from django.apps import AppConfig


class DivisionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'division'

    def ready(self):
        # pylint: disable=C0415
        import division.signals
