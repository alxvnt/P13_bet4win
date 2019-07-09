from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('connexion', views.connection, name='connection'),
    path('enregistrement', views.register, name='register'),
    path('deco', views.disconnection, name='disconnect'),

]