from django.urls import path
from . import views

urlpatterns = [
    path('scale', views.scaleImage)
]
