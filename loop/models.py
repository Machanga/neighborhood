from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length = 60)
    neighborhood_location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.neighborhood_name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()

class Location(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50,null=True)
    ID = models.IntegerField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 60)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    name = models.CharField(max_length = 60)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 60)
    
    def __str__(self):
        return self.name
    
    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self):
        self.save()

class Post(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)

    def __str__(self):
        return self.title
