from django.urls import path
from . import views


urlpatterns = [
    path('PROTOCOL', views.Protocol, name="PROTOCOL"),
    path('PROTOCOL/<str:lang>/<str:sop>/<str:title>', views.sop_detail, name='sop_detail'),
]