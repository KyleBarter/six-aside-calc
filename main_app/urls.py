from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('players/', views.index, name='index'),
    path('players/<int:player_id>', views.index, name='index'),
    path('teams/', views.index, name='index'),
]