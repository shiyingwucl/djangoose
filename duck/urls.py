from django.urls import path

from . import views

app_name = 'duck'

urlpatterns = [
    path('',views.pokemon_list,name='pokemon_list')
]