import csv
import logging
import os
import random
import re
import sys

from collections import deque
from pathlib import Path
from typing import Any, Generator

from tqdm import tqdm

from .config import Config
from .downloader import Downloader
from .types.segment_type import SegmentType
from .utils import cli_utils, file_utils, time_utils
from .writer import Writer


try:
  import requests

  from .recognizers.wit_recognizer import WitRecognizer
  from .utils.wit import file_utils as wit_file_utils
except ModuleNotFoundError:
  pass


try:
  from .recognizers.whisper_recognizer import WhisperRecognizer
  from .types.whisper.type_hints import WhisperModel
  from .utils.whisper import whisper_utils
except ModuleNotFoundError:
  pass


def main():
  args = cli_utils.parse_args(sys.argv[1:])

  config = Config(
    input=Config.Input(
      urls_or_paths=args.urls_or_paths,
      skip_if_output_exist=args.skip_if_output_exist,
      download_retries=args.download_retries,
      yt_dlp_options=args.yt_dlp_options,
      verbose=args.verbose,
    ),
    whisper=Config.Whisper(
      model_name_or_path=args.model_name_or_path,
      task=args.task,
      language=args.language,
      use_faster_whisper=args.use_faster_whisper,
      beam_size=args.beam_size,
      ct2_compute_type=args.ct2_compute_type,
    ),
    wit=Config.Wit(
      wit_client_access_tokens=args.wit_client_access_tokens,
      max_cutting_duration=args.max_cutting_duration,
    ),
    output=Config.Output(
      min_words_per_segment=args.min_words_per_segment,
      save_files_before_compact=args.save_files_before_compact,
      save_yt_dlp_responses=args.save_yt_dlp_responses,
      output_sample=args.output_sample,
      output_formats=args.output_formats,
      output_dir=args.output_dir,
    ),
  )

  if config.use_wit() and config.input.skip_if_output_exist:
    retries = 3

    while retries > 0:
      try:
        deque(farrigh(config), maxlen=0)
        break
      except requests.exceptions.RetryError:
        retries -= 1
  else:
    deque(farrigh(config), maxlen=0)


def farrigh(config: Config) -> Generator[dict[str, Any], None, None]:
  prepare_output_dir(config.output.output_dir)

  model = None
  if not config.use_wit():
    model = whisper_utils.load_model(config.whisper)

  segments: list[SegmentType] = []

  for idx, item in enumerate(tqdm(config.input.urls_or_paths, desc='URLs or local paths')):
    progress_info = {
      'outer_total': len(config.input.urls_or_paths),
      'outer_current': idx + 1,
      'outer_status': 'processing',
    }

    if Path(item).exists():
      file_or_folder = Path(item)
      for progress_info, local_elements_segments in process_local(file_or_folder, model, config, progress_info):
        segments.extend(local_elements_segments)
        yield progress_info
    elif re.match('(https?://)', item):
      for progress_info, url_elements_segments in process_url(item, model, config, progress_info):
        segments.extend(url_elements_segments)
        yield progress_info
    else:
      logging.error(f'Path {item} does not exist and is not a URL either.')

      progress_info['outer_status'] = 'completed'
      yield progress_info

      continue

    progress_info['outer_status'] = 'completed'
    yield progress_info

  write_output_sample(segments, config.output)


def prepare_output_dir(output_dir: str) -> None:
  os.makedirs(output_dir, exist_ok=True)


def process_local(
  path: Path,
  model: 'WhisperModel',
  config: Config,
  progress_info: dict,
) -> Generator[tuple[dict[str, Any], list[SegmentType]], None, None]:
  filtered_media_files = file_utils.filter_media_files([path] if path.is_file() else list(path.iterdir()))
  files: list[dict[str, Any]] = [{'file_name': file.name, 'file_path': file} for file in filtered_media_files]

  for idx, file in enumerate(tqdm(files, desc='Local files')):
    new_progress_info = progress_info.copy()
    new_progress_info.update(
      {
        'inner_total': len(files),
        'inner_current': idx + 1,
        'inner_status': 'processing',
        'progress': 0.0,
        'remaining_time': None,
      }
    )
    yield new_progress_info, []

    writer = Writer()
    if config.input.skip_if_output_exist and writer.is_output_exist(Path(file['file_name']).stem, config.output):
      new_progress_info['inner_status'] = 'completed'
      yield new_progress_info, []

      continue

    file_path = str(file['file_path'].absolute())

    if config.use_wit():
      mp3_file_path = str(wit_file_utils.convert_to_mp3(file['file_path']).absolute())
      recognize_generator = WitRecognizer(verbose=config.input.verbose).recognize(mp3_file_path, config.wit)
    else:
      recognize_generator = WhisperRecognizer(verbose=config.input.verbose).recognize(
          file_path,
          model,
          config.whisper,
      )

    while True:
      try:
        new_progress_info.update(next(recognize_generator))
        yield new_progress_info, []
      except StopIteration as exception:
        segments: list[SegmentType] = exception.value
        break

    if config.use_wit() and file['file_path'].suffix != '.mp3':
      Path(mp3_file_path).unlink(missing_ok=True)

    writer.write_all(Path(file['file_name']).stem, segments, config.output)

    for segment in segments:
      segment['url'] = f"file://{file_path}&t={int(segment['start'])}"
      segment['file_path'] = file_path

    new_progress_info['inner_status'] = 'completed'
    new_progress_info['progress'] = 100.0
    yield new_progress_info, writer.compact_segments(segments, config.output.min_words_per_segment)


def process_url(
  url: str,
  model: 'WhisperModel',
  config: Config,
  progress_info: dict,
) -> Generator[tuple[dict[str, Any], list[SegmentType]], None, None]:
  url_data = Downloader(yt_dlp_options=config.input.yt_dlp_options, output_dir=config.output.output_dir).download(
    url,
    retries=config.input.download_retries,
    save_response=config.output.save_yt_dlp_responses,
  )

  elements = [url_data]

  if url_data.get('_type', '') == 'playlist':
    entries = url_data['entries']
    elements = []

    for entry in entries:
      if entry.get('_type', '') == 'playlist':
        elements.extend(entry['entries'])
      else:
        elements.append(entry)

    elements = list(filter(lambda element: element, elements))

  for idx, element in enumerate(tqdm(elements, desc='URL elements')):
    if should_skip(element):
      continue

    new_progress_info = progress_info.copy()
    new_progress_info.update({
      'inner_total': len(elements),
      'inner_current': idx + 1,
      'inner_status': 'processing',
      'progress': 0.0,
      'remaining_time': None,
    })
    yield new_progress_info, []

    writer = Writer()
    if config.input.skip_if_output_exist and writer.is_output_exist(element['id'], config.output):
      new_progress_info['inner_status'] = 'completed'
      yield new_progress_info, []

      continue

    file_path = os.path.join(config.output.output_dir, f"{element['id']}.mp3")

    if config.use_wit():
      recognize_generator = WitRecognizer(verbose=config.input.verbose).recognize(file_path, config.wit)
    else:
      recognize_generator = WhisperRecognizer(verbose=config.input.verbose).recognize(
        file_path,
        model,
        config.whisper,
      )

    while True:
      try:
        new_progress_info.update(next(recognize_generator))
        yield new_progress_info, []
      except StopIteration as exception:
        segments: list[SegmentType] = exception.value
        break

    writer.write_all(element['id'], segments, config.output)

    for segment in segments:
      segment['url'] = f"https://youtube.com/watch?v={element['id']}&t={int(segment['start'])}"
      segment['file_path'] = file_path

    new_progress_info['inner_status'] = 'completed'
    new_progress_info['progress'] = 100.0
    yield new_progress_info, writer.compact_segments(segments, config.output.min_words_per_segment)


def write_output_sample(segments: list[SegmentType], output: Config.Output) -> None:
  if output.output_sample == 0:
    return

  random.shuffle(segments)

  with open(os.path.join(output.output_dir, 'sample.csv'), 'w') as fp:
    writer = csv.DictWriter(fp, fieldnames=['start', 'end', 'text', 'url', 'file_path'])
    writer.writeheader()

    for segment in segments[:output.output_sample]:
      formatted_start = time_utils.format_timestamp(segment['start'], include_hours=True, decimal_marker=',')
      formatted_end = time_utils.format_timestamp(segment['end'], include_hours=True, decimal_marker=',')

      writer.writerow({
        'start': formatted_start,
        'end': formatted_end,
        'text': segment['text'],
        'url': segment['url'],
        'file_path': segment['file_path'],
      })


def should_skip(element: dict[str, Any]) -> bool:
  return (element['title'] == '[Private video]' or
          element['title'] == '[Deleted video]' or
          ('availability' in element and element['availability'] == 'subscriber_only') or
          ('live_status' in element and element['live_status'] == 'is_upcoming'))
