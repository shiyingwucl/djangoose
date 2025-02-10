from django.contrib import admin
from .models import Pokemon, Moveset, Move
# Register your models here.

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Moveset)
class MovesetAdmin(admin.ModelAdmin):

    def safe_moveset(self, obj):
        return str(obj.moveset.moves.all())
    
    list_display = (safe_moveset,)

    

@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ("name",)
#class MovesetAdmin(admin.ModelAdmin):