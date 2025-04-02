# china_division/__init__.py
from .core import get_division_info, search_division, get_parent_division, get_child_divisions

__all__ = [
    'get_division_info',
    'search_division',
    'get_parent_division',
    'get_child_divisions'
]

__version__ = '2.0'
