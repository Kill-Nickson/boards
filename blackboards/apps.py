from django.apps import AppConfig


class BlackboardsConfig(AppConfig):
    name = 'blackboards'

    def ready(self):
        import blackboards.signals
