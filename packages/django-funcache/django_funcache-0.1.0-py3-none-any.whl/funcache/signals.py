from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save)
def invalidate_cache(sender, instance, created, **kwargs):
    if hasattr(settings, "INVALIDATE_CACHE_REGISTRY"):
        cache_registry = settings.INVALIDATE_CACHE_REGISTRY
        model_keys = cache_registry.get(sender.__name__)
        if model_keys:
            for key in model_keys:
                cache.delete(key)