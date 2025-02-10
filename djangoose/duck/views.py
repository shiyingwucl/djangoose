from django.http import HttpResponse
from django.shortcuts import render

from .models import Pokemon
# Create your views here.

def index(request):
    return HttpResponse("Hi")

def dynamic_data_view(request):
    # Retrieve dynamic data from the model
    pokemon = Pokemon.objects.all()

     # Define a context dictionary variable and Pass the dynamic data to the template
    context = {
        'pokemon_name': pokemon.name,
        'pokemon_movesets': pokemon.moveset.all(),
        }

    # Render the template with the dynamic data
    return render(request, 'sample_template.html', context)