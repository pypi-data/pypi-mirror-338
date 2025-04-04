__version__ = "0.5.6"
__version_tuple__ = (0, 5, 6)

from . core.io import (
    get_loader,
    get_writer,
    save,
)

__all__ = [
    'get_loader',
    'get_writer',
    'save',
]
