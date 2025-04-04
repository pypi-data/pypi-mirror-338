"""Django function caching and temporary file permissions."""

__version__ = '0.1.0'
default_app_config = 'funcache.apps.FuncacheConfig'

# Import in a way that works for both Python 2 and 3
from funcache.utils import func_cache, cache_key_register