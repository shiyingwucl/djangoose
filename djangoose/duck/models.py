from django.db import models

# Create your models here.
    
class Move(models.Model):
    def __str__(self):
        return f"{self.name}"
    name = models.CharField(max_length=60,blank=False)
    damage = models.IntegerField()
    accuracy = models.FloatField(max_length=4)

class Moveset(models.Model):
    def __str__(self):
        return f"{self.moveset.all()}"
    first_move = models.ManyToManyField(Move,related_name="first_move")
    second_move = models.ManyToManyField(Move,related_name="second_move")
    third_move = models.ManyToManyField(Move,related_name="third_move")
    fourth_move = models.ManyToManyField(Move,related_name="fourth_move")

class Pokemon(models.Model):
    def __str__(self):
        return f"{self.name},{self.moveset.all()}"
    
    name = models.CharField(max_length=60,blank=False) 
    #blank makes sure the property has to have a name, blank is admin, null is database 

    moveset = models.ManyToManyField(Moveset,related_name="moveset",)
    # figure out how to limit many to many relationships
    # when moves are = 4, set can_get_moves to False, <4 set to True
    