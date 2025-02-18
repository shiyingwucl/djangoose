from django.db import models

# Create your models here.
class Pokemon(models.Model):

    name = models.CharField(max_length=60,blank=False)
    type = models.ForeignKey("Type",related_name="pokemon_type",blank=True,on_delete=models.SET_NULL, null=True)
    first_move = models.ForeignKey("Move",related_name="first_move",blank=True,on_delete=models.SET_NULL, null=True)
    second_move = models.ForeignKey("Move",related_name="second_move",blank=True,on_delete=models.SET_NULL, null=True)
    third_move = models.ForeignKey("Move",related_name="third_move",blank=True,on_delete=models.SET_NULL, null=True)
    fourth_move = models.ForeignKey("Move",related_name="fourth_move",blank=True,on_delete=models.SET_NULL, null=True)
    
    # blank makes sure the property has to have a name, blank is admin, null is database
    # figure out how to limit many to many relationships

    def __str__(self):
        return self.name
class Move(models.Model):

    name = models.CharField(max_length=60,blank=False)
    damage = models.IntegerField()
    accuracy = models.FloatField(max_length=4)
    type = models.ForeignKey("Type",related_name="move_type",blank=False,on_delete=models.SET_NULL,null=True)

    @property
    def pokemon_count(self):
        return Pokemon.objects.filter(
            models.Q(first_move=self) |
            models.Q(second_move=self) |
            models.Q(third_move=self) |
            models.Q(fourth_move=self) 
        ).distinct().count()

    def __str__(self):
        return self.name

class Type(models.Model):

    name = models.CharField(max_length=30,blank=False)
    super_effective = models.ForeignKey("self",related_name="supereffective",on_delete=models.CASCADE,null=True,blank=True)
    not_very_effective = models.ForeignKey("self",related_name="notveryeffective",on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
