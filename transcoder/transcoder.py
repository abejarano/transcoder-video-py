import os
import tempfile
from converter import Converter


def make_convert(source_video, video_name, version):
    video_name = version + '_' + video_name
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
                'width': 640,
                'height': 480,
            }
        },
        timeout=False
    )

    for time_code in conv:
        time_code

    print("3-. processed video")
    return [destination, video_name]
