from django.apps import AppConfig


class SeoappConfig(AppConfig):
    name = 'seoapp'
    verbose_name = 'Configurações seo'

    def ready(self):
        import seoapp.signals
