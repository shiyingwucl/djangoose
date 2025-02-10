from django.urls import path

from . import views

app_name = 'duck'

urlpatterns = [
    path('duck/',views.index,name='index')
]