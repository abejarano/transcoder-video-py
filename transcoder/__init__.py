import logging
import os

from google.cloud import storage

from transcoder.transcoder import make_convert

storage_client = storage.Client()


def extract_version_from_name(file_name) -> str:
    name = file_name.split("_")
    return name[0]


def generate_version(version, bucket, temp_file_path, file_name):
    [path_new_video, name_video] = make_convert(
        temp_file_path,
        file_name,
        version
    )

    if path_new_video is None:
        return

    blob = bucket.blob(name_video)
    blob.upload_from_filename(path_new_video)

    print("4-. Uploaded file " + path_new_video)

    os.remove(path_new_video)


def logger():
    mod_name = 'transcoder'
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
