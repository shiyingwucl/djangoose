from django.contrib import admin
from .models import Pokemon, Move
# Register your models here.


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ("name",)
#class MovesetAdmin(admin.ModelAdmin):
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ...