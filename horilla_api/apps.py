from django.apps import AppConfig


class EVOTEM HRApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "evotem_hr_api"

    def ready(self):
        from django.urls import include, path

        from horilla.urls import urlpatterns

        urlpatterns.append(
            path("api/", include("evotem_hr_api.urls")),
        )
        super().ready()
