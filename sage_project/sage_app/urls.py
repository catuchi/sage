from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),        # home page
  path('room/<str:pk>/', views.room, name='room'),
]