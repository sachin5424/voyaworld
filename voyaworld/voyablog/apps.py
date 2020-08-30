from django.apps import AppConfig


class VoyablogConfig(AppConfig):
    name = 'voyablog'
    def ready(self):
        import voyablog.mysingnals
