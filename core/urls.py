from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_analytics/', views.data_analytics, name='data_analytics'),
    path('data_visualization/', views.data_visualization, name='data_visualization'),
    path('big_data/', views.big_data, name='big_data'),
    path('economic_analysis/', views.economic_analysis, name='economic_analysis'),
    path('data_analysis/', views.data_analysis, name='data_analysis'),
]