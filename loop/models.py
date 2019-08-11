from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length = 60)
    neighborhood_location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User,on_delete = models.CASCADE)

