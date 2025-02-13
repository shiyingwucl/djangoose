from django.db import models

# Create your models here.
class Move(models.Model):

    name = models.CharField(max_length=60,blank=False)
    damage = models.IntegerField()
    accuracy = models.FloatField(max_length=4)
    type = models.ForeignKey("Type",related_name="move_type",blank=False,on_delete=models.SET_NULL,null=True)
    pokemon_count = 0
    def __str__(self):
        return self.name
    
    def count(self):
        pokemons = Pokemon.objects.all()
        
        for pokemon in pokemons:
            if self in [pokemon.first_move, pokemon.second_move, pokemon.third_move, pokemon.fourth_move]:
                self.pokemon_count += 1
                
        # 1. get all pokemons
        # 2. see if any of the first/second/third/fourth move in each reference self
        # 3. if yes, count +=1
        # 4. return the integer
        # 5. set this to an attribute and display via admin.py
    
class Type(models.Model):

    name = models.CharField(max_length=30,blank=False)
    
    def __str__(self):
        return self.name

#class TypeRelationship():
#
#    type = Type
#    super_effective = list[Type]
#    not_very_effective = list[Type]

class Pokemon(models.Model):

    name = models.CharField(max_length=60,blank=False)
    type = models.ForeignKey(Type,related_name="pokemon_type",blank=True,on_delete=models.SET_NULL, null=True)
    first_move = models.ForeignKey(Move,related_name="first_move",blank=True,on_delete=models.SET_NULL, null=True)
    second_move = models.ForeignKey(Move,related_name="second_move",blank=True,on_delete=models.SET_NULL, null=True)
    third_move = models.ForeignKey(Move,related_name="third_move",blank=True,on_delete=models.SET_NULL, null=True)
    fourth_move = models.ForeignKey(Move,related_name="fourth_move",blank=True,on_delete=models.SET_NULL, null=True)
    
    # blank makes sure the property has to have a name, blank is admin, null is database
    # figure out how to limit many to many relationships

    def __str__(self):
        return self.name
    
