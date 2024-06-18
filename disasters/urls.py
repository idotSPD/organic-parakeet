from django.urls import path
from . import views

urlpatterns = [
    path('', views.disaster_list, name='disaster_list'),
    path('<int:pk>/', views.disaster_detail, name='disaster_detail'),
]
