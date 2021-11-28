import datetime
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from decouple import config
from google.cloud.pubsub_v1.subscriber.message import Message

from cache.redis import Redis
from transcoder import logger
from transcoder.main import transcoder

subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path(
    config('PROJECT_ID'),
    config('SUBSCRIPTION_ID')
)

cache = Redis()


def process_message(message: Message) -> None:
    message.ack()

    today = datetime.date.today()

    attr_file = {
        "bucketId": message.attributes.get('bucketId'),
        "eventTime": today,
        "objectId": message.attributes.get('objectId')
    }

    if message.attributes.get('eventType') != 'OBJECT_FINALIZE':
        return

    if cache.exists_file_in_cache(attr_file):
        return

    print('Video ' + attr_file['objectId'] + ' receive')

    transcoder(
        attr_file['bucketId'],
        attr_file['objectId']
    )


streaming_pull_future = subscriber.subscribe(subscription_path, callback=process_message)

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError as e:
        logger().debug(
            f"Listening for messages on {subscription_path} threw an exception: {e}."
        )

        streaming_pull_future.cancel()
        streaming_pull_future.result()
