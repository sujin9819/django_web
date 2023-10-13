from django.urls import path
from . import views


urlpatterns = [
    path('PROTOCOL', views.Protocol, name="PROTOCOL"),
]