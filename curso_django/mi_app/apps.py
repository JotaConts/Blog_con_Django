from django.apps import AppConfig


class MiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mi_app'
    # Cambiar nombre en el panel admin
    verbose_name = 'Mi primera app'
