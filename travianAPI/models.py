from django.db import models

# Create your models here.
class Materials(models.Model):
    name = models.CharField(max_length=60)
    size = models.IntegerField(default = 0,blank = True,editable = True)
    def __str__(self):
        return self.name

class Troops(models.Model):
    name = models.CharField(max_length=60)
    attack = models.IntegerField(default = 0, blank = True, editable = True)
    defence_infantry = models.IntegerField(default = 0, blank = True, editable = True)
    defence_cavalry = models.IntegerField(default = 0, blank = True, editable = True)
    speed = models.IntegerField(default = 0, blank = True, editable = True)
    carrying_capacity = models.IntegerField(default = 0, blank = True, editable = True)
    crop_consumption = models.IntegerField(default = 0, blank = True, editable = True)
    troops_size = models.IntegerField(default = 0, blank = True, editable = True)
    def __str__(self) -> str:
        return super().__str__()