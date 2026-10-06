from django.urls import path
from . import views

urlpatterns = [
    path("", views.reviews),  # type: ignore
    path("thank-you", views.thank_you),
]
