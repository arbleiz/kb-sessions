from django.urls import path
from api.views import ninja_api

urlpatterns = [
    path("api/", ninja_api.urls)
]