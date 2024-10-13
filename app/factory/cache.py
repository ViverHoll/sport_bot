from cachetools import TTLCache


def create_ttl_cache() -> TTLCache:
    return TTLCache(
        maxsize=100_000,
        ttl=20
    )
