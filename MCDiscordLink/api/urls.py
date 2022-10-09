from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r"^players$", views.players_list),
    re_path(r"players/(?P<pk>[0-9]+)$", views.players_detail),
    re_path(r"^players/linked$", views.players_linked),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
]
