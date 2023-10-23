from django.urls import path
from . import views


urlpatterns = [
    path('PROTOCOL', views.Protocol, name="PROTOCOL"),
    path('PROTOCOL/en/<str:sop>/<str:title>', views.sop_detail_en, name='sop_detail_en'),
    path('PROTOCOL/ko/<str:sop>/<title>', views.sop_detail_ko, name='sop_detail_ko'),
    path('PROTOCOL/ko', views.Protocol_ko, name='Protocol_ko'),
]