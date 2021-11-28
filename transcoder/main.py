import os
import tempfile
import time

from transcoder import storage_client, extract_version_from_name, generate_version


def get_version_generated(file_name: str) -> object:
    extract_version = extract_version_from_name(file_name)
    if extract_version.find('1280x720') == 0:
        return ['640x480', file_name.replace('1280x720_', '')]

    elif extract_version.find('640x480') == 0:
        print('Video ' + extract_version + ' has already been processed')
        return ['', file_name]

    return ['1280x720', file_name]


def transcoder(bucket_id, file_name):
    version, file_name = get_version_generated(file_name)

    if version == '':
        return

    temp_file_path = os.path.join(tempfile.gettempdir(), file_name)

    print(temp_file_path)

    bucket = storage_client.bucket(bucket_id)

    print("1-. Downloading the original video")

    blob = bucket.blob(file_name)
    blob.download_to_filename(temp_file_path)

    start_time = time.time()

    generate_version(
        version,
        bucket,
        temp_file_path,
        file_name
    )

    os.remove(temp_file_path)

    print("--- %s finish ---" % (time.time() - start_time))
