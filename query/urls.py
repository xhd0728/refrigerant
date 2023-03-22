from django.urls import path
from . import views

urlpatterns = [
    path("params", views.ParamsQueryView.as_view()),
]
