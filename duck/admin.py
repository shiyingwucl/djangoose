from django.contrib import admin
from .models import Pokemon, Move, Type
# Register your models here.


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ("name","type")
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name","type","first_move","second_move","third_move","fourth_move")

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name",)