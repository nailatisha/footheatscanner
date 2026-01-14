from django.urls import path
from .views import show_scanner

urlpatterns = [
    path("", show_scanner),
]
