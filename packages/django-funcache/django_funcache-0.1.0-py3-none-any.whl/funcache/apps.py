from django.apps import AppConfig


class FuncacheConfig(AppConfig):
    name = 'funcache'
    verbose_name = 'Django Function Cache'
    
    def ready(self):
        """Run code when the app is ready."""
        # Import the tempfile patch module
        import funcache.signals  # noqa
