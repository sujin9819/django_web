from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('Home', views.index, name="Home"),
    path('About',views.About, name="About"),
    path('Gene',views.Gene, name="Gene"),
    path('Genome',views.Genome, name="Genome"),
    path('Samples',views.Samples,name="Samples"),
    path('Genome/<pk>', views.MAG_detail, name='MAG_detail'),
    path('search', views.search, name='search'),
]