from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('players/', views.get_players, name='players'),
    path('players/<int:player_id>', views.get_individual_player, name='player'),
    path('teams/', views.index, name='index'),
]