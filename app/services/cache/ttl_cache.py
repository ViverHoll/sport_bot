
from cachetools import TTLCache


class Cache(TTLCache):
    def __init__(
            self,
            max_size: int,
            ttl: float,
    ) -> None:
        super().__init__(
            maxsize=max_size,
            ttl=ttl,
        )

    def check_key(self, key) -> bool:
        return self.get(key, False)





if __name__ == "__main__":
    c = Cache(10, 1.0)
    # print(c.check_key("53"))

