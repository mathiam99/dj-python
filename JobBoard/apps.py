from django.apps import AppConfig


class JobboardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "JobBoard"

#   def ready(self):
#        import JobBoard.signals
