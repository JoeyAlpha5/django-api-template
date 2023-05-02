from django.urls import path, include

urlpatterns = [
    path("v0/", include("api.v0.health.urls")),
    path("v1/", include("api.v1.health.urls")),
    path("", include("api.v0.health.urls")),
]
