import time

class Cache:
    """ In-memory cache with expiration. """

    def __init__(self):
        self.cache = {}
        self.expiration_time = 300 # 5 minutes

    def set(self, key: str | None, value: str):
        if key is None:
            return

        self.cache[key] = (value, time.time() + self.expiration_time)

    def get(self, key: str | None) -> str | None:
        if key is None:
            return None

        if key in self.cache:
            value, expiration = self.cache[key]

            if time.time() < expiration:
                return value

            del self.cache[key]

        return None
