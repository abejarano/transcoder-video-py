import os
import platform
import tempfile
from converter import Converter


def get_size_video(version: str) -> object:
    return version.split('x')


def make_convert(source_video, video_name, version):
    video_name = version + '_' + video_name
    width, height = get_size_video(version)
    destination = os.path.join(tempfile.gettempdir(), video_name)

    print("2-. In processing convert")
    c = Converter()

    conv = c.convert(
        source_video,
        destination,
        {
            'format': 'mp4',
            'audio': {
                'codec': 'aac',
                'channels': 2
            },
            'video': {
                'codec': 'hevc',
                'width': width,
                'height': height,
            }
        },
        timeout=False
    )

    for time_code in conv:
        time_code

    print("3-. processed video")

    return [destination, video_name]


def get_name_file(file_path: str) -> str:
    if platform.system() == 'Windows':
        array_name = file_path.split("\\")
    else:
        array_name = file_path.split("/")

    return array_name[len(array_name) - 1]


def __main__(file_path: str):
    versions = ['480x854', '720x1280']

    temp_file_path = os.path.join(tempfile.gettempdir(), file_path)

    for version in versions:
        make_convert(
            temp_file_path,
            get_name_file(file_path),
            version
        )


__main__()
