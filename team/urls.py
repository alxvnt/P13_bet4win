from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('nouvelle-team', views.new_team, name='new_team'),
    path('', views.my_groups, name='my_groups'),
    path('mes-groupes', views.my_groups, name='my_groups'),
    path('rejoindre-team', views.join_group, name='join_group'),
    path('quitter-team', views.leave_team, name='leave_team'),
    path('erreur-team', views.team_error, name='error-team'),
    path('classement/<str:team_name>/', views.ranking_team, name='ranking'),
    path('championnat/<str:team_name>/', views.champ, name='champ'),
    path('match/<str:team_name>/', views.match_to_bet, name='match'),
    path('calendrier/<str:team_name>', views.day_match, name='day_match'),
    path('pari/<str:team_name>/<str:id_match>/<str:prono>', views.my_bet, name='my_bet')

]