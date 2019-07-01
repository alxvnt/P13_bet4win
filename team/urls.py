from django.conf.urls import url

from . import views

urlpatterns = [
    url('test', views.test, name='test'),
    url('nouvelle-team', views.new_team, name='new_team'),
    url('mes-groupes', views.my_groups, name='my_groups'),
    url('rejoindre-team', views.join_group, name='join_group')
]