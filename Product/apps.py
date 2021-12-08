from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Product'


    def ready(self):
        from Product.pythonScripts import updater
        print('starting')
        updater.start()