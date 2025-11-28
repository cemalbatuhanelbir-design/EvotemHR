from django.urls import include, path

urlpatterns = [
    path("auth/", include("evotem_hr_api.api_urls.auth.urls")),
    path("asset/", include("evotem_hr_api.api_urls.asset.urls")),
    path("base/", include("evotem_hr_api.api_urls.base.urls")),
    path("employee/", include("evotem_hr_api.api_urls.employee.urls")),
    path("notifications/", include("evotem_hr_api.api_urls.notifications.urls")),
    path("payroll/", include("evotem_hr_api.api_urls.payroll.urls")),
    path("attendance/", include("evotem_hr_api.api_urls.attendance.urls")),
    path("leave/", include("evotem_hr_api.api_urls.leave.urls")),
]
