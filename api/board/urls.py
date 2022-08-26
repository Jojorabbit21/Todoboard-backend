from django.urls import path, include
from . import views

urlpatterns = [
  # Board API
  path('get/board/', views.api_board),
  path('post/board/', views.api_board),
  # Agenda API
  path('get/agenda/', views.api_agenda),
  path('post/agenda/', views.api_agenda),
]