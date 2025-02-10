from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon
# Create your views here.

def index(request):
    return HttpResponse("Hi")

def pokemon_list(request):

    # query all pokemon objects?
    pokemons = Pokemon.objects.all()

    context = {
        'pokemons': pokemons,
        }

    # render template
    return render(request, 'test.html', context)