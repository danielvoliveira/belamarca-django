from django.apps import AppConfig


class BannerappConfig(AppConfig):
    name = 'bannerapp'
    verbose_name = 'banners'

    def ready(self):
        import bannerapp.signals
