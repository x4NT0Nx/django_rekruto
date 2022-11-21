from django.urls import path
from hello_rekruto import views

urlpatterns = [
    path("", views.index),
]
