from django.apps import AppConfig


class ProductappConfig(AppConfig):
    name = 'productapp'
    verbose_name = 'Produtos'

    def ready(self):
        import productapp.signals