# For Python 2/3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals

try:
    # Python 3
    from typing import Any, Callable, Union, List
except ImportError:
    # Python 2 - define dummy types
    Any = Callable = Union = List = None

from django.core.cache import cache
from django.conf import settings
from functools import wraps

CACHE_KEY_SEPARATOR = "_"
DEFAULT_CACHE_SUFFIX = "cache"

def get_cache_timer():
    """Get cache timeout from settings or set default."""
    if hasattr(settings, 'CACHE_TIMER'):
        return settings.CACHE_TIMER
    else:
        settings.CACHE_TIMER = 1800
        return 1800


def cache_key_register(model_name, key_name):
    """Add a cache key to the invalidation map for a model."""
    # Initialize INVALIDATE_CACHE_MAP if it doesn't exist
    if not hasattr(settings, "INVALIDATE_CACHE_REGISTRY"):
        settings.INVALIDATE_CACHE_REGISTRY = {}
    
    cache_registry = settings.INVALIDATE_CACHE_REGISTRY
    model_keys = cache_registry.get(model_name)
    
    # If model already has keys and this key is already in the list, do nothing
    if isinstance(model_keys, list):
        if key_name not in model_keys:
            model_keys.append(key_name)
    else:
        # Create a new list for this model
        cache_registry[model_name] = [key_name]


def func_cache(key_prefix):
    """
    Take a function with parameters and cache the result
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create a more efficient cache key
            parts = [func.__name__]
            if args:
                parts.append("_".join(str(arg) for arg in args))
            if kwargs:
                parts.append("_".join("{0}_{1}".format(k, v) for k, v in sorted(kwargs.items())))
            parts.append("smarttax")
            
            cache_key = "_".join(parts)
            result = cache.get(cache_key)
            
            if result is None:
                result = func(*args, **kwargs)
                # Use the constant from get_cache_timer instead of hardcoded 30 minutes
                cache_timeout = get_cache_timer()
                cache.set(cache_key, result, cache_timeout)
                
                # Register the cache key for invalidation
                if isinstance(key_prefix, list):
                    for key in key_prefix:
                        cache_key_register(key, cache_key)
                elif key_prefix:  # Check if key_prefix is not empty
                    cache_key_register(key_prefix, cache_key)
            return result
        return wrapper
    return decorator
