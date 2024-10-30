from .dao.holder import HolderDAO
from .middleware import DatabaseMiddleware

Database = HolderDAO

__all__ = [
    "HolderDAO",
    "DatabaseMiddleware",
    "Database",
]
