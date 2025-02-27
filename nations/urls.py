from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('region/', views.region, name='region'),
    path('subregion/', views.subregion, name='subregion'),  
    path('country/', views.country, name='country'),
    path('state/', views.state, name='state'),
    path('city/', views.city, name='city'),

]