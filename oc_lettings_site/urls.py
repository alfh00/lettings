from django.contrib import admin
from django.urls import include, path
from sentry_sdk import set_level

from . import views

set_level("warning")


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
