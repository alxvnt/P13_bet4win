from django.conf.urls import url

from . import views

urlpatterns = [
    url('nouvelle-team', views.new_team, name='new_team'),
    url('mes-groupes', views.my_groups, name='my_groups'),
    url('rejoindre-team', views.join_group, name='join_group'),
    url('quitter-team', views.leave_team, name='leave_team'),
    url('erreur-team', views.team_error, name='error-team'),
    url('classement/', views.ranking_team, name='ranking'),
]