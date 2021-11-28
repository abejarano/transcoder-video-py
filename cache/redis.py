import redis
from decouple import config


class Redis:
    __instance = None

    def __new__(cls):
        if Redis.__instance is None:
            Redis.__instance = object.__new__(cls)

        return Redis.__instance

    def __init__(self):
        self.__cache = redis.Redis(host=config('REDIS_SERVER'), port=config('REDIS_PORT'), db=0)

    def save_to_cache(self, attr_file: dict) -> None:
        self.__cache.sadd(attr_file['objectId'], *attr_file)

    def exists_file_in_cache(self, attr_file: dict) -> bool:
        cache_file = self.__cache.smembers(attr_file['objectId'])

        return cache_file != set()
