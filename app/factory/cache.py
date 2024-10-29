from cachetools import TTLCache


def create_ttl_cache(
        *,
        max_size: int,
        ttl: int
) -> TTLCache:
    return TTLCache(
        maxsize=max_size,
        ttl=ttl
    )
