# Django FunCache

A Django app providing function-level caching with parameter-based keys and fixes for temporary file permissions.

## Features

- Function-level caching with parameter-based cache keys
- Automatic cache key invalidation
- Compatible with Python 2.7 and Python 3.x
- Works with Django 1.11 and higher

## Installation

```bash
# Using pip
pip install django-funcache
```

```bash
# Using uv
uv add django-funcache
```

Add to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'funcache',
    ...
]
```

## Usage

### Function Caching

Set the cache key prefix for a specific model or a set of models to invalidate the cache when the model datas are updated.


```python
from funcache import func_cache
# Using for a specific model
@func_cache(key_prefix='my_model')
def expensive_function(param1, param2):
    # Function code here
    return result

# Using for a set of models
@func_cache(key_prefix=['my_model1', 'my_model2'])
def expensive_function(param1, param2):
    # Function code here
    return result
```

The cache invalidator is managed by the `funcache` app through a signal.

## Settings

You can customize the cache timeout:

```python
# In settings.py
CACHE_TIMER = 1800  # 30 MINUTES (default is 1800 seconds/30 minutes)
```

## Python 2 and 3 Compatibility

This package works with both Python 2.7 and Python 3.x environments. It's tested with:

- Python 2.7 with Django 1.11
- Python 3.6+ with Django 2.2, 3.2, and 4.x

## License

MIT
