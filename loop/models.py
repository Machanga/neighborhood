from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length = 60)
    neighborhood_location = models.CharField(max_length = 60)
    occupants = models.IntegerField()

