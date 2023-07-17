from django.apps import AppConfig


class GenericappConfig(AppConfig):
    name = 'genericapp'
    verbose_name = 'Genéricos'

    def ready(self):
        import genericapp.signals
