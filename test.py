import os
import platform
import tempfile
from converter import Converter


def get_size_video(version: str) -> object:
    return version.split('x')


def make_convert(source_video, video_name, version, destination):
    video_name = version + '_' + video_name
    width, height = get_size_video(version)
    destination = os.path.join(destination, video_name)

    print(destination)


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


def get_name_and_path_file(file_path: str) -> str:
    if platform.system() == 'Windows':
        array_name = file_path.split("\\")
    else:
        array_name = file_path.split("/")
    name = array_name[len(array_name) - 1]
    return [
        name,
        file_path.replace(name, '')
    ]


def __main__(file_path: str):
    versions = ['854x480', '1280x720']

    [file_name, destination] = get_name_and_path_file(file_path)

    for version in versions:
        make_convert(
            file_path,
            file_name,
            version,
            destination
        )


__main__('path_file')
