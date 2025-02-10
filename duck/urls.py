from django.urls import path

from . import views

app_name = 'duck'

urlpatterns = [
    path('list/',views.pokemon_list,name='index')
]