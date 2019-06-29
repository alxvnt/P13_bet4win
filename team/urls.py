from django.conf.urls import url

from . import views

urlpatterns = [
    url('test', views.test, name='test'),
    url('nouvelle-team', views.new_team, name='new_team'),
]