from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon, Move
# Create your views here.

def index(request):
    return HttpResponse("Hi")

def pokemon_list(request):

    # query all pokemon objects?
    pokemons:Pokemon = Pokemon.objects.all()
    moves = Move.objects.all()

    context = {
        'moves': moves,
        'pokemons': pokemons,
        }

    # render template
    return render(request, 'template.html', context)

