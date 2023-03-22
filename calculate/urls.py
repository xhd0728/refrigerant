from django.urls import path
from . import views

urlpatterns = [
    path("params", views.ParamsCalculateView.as_view()),
]
