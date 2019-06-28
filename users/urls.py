from django.conf.urls import url

from . import views

urlpatterns = [
    url('connexion', views.connection, name='connection'),
    url('enregistrement', views.register, name="register"),

]