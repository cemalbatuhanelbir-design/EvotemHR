from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project"

    def ready(self):
        from django.urls import include, path

        from horilla.evotem_hr_settings import APP_URLS, APPS
        from horilla.urls import urlpatterns

        APPS.append("project")
        urlpatterns.append(
            path("project/", include("project.urls")),
        )
        APP_URLS.append("project.urls")
        super().ready()
