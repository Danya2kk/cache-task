from django.apps import AppConfig


class CacheExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cache_example'

    def ready(self):
        import cache_example.signals
