from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighborhood
# Create your tests here.

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='qwerty12345')
        self.location = Location(id=1,name='Test name')
        self.neighborhood = Neighborhood(id=1,neighborhood_name='Test name',neighborhood_location=self.location,admin=self.user, occupants=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood,Neighborhood))

    def test_create_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) > 0)

    def test_delete_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.neighborhood = Neighborhood.objects.get(id=1)
        self.neighborhood.delete_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) == 0)

    def test_find_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.searched_neighborhood = Neighborhood.find_neighborhood(1)
        self.assertTrue(self.searched_neighborhood == self.neighborhood)

    def test_update_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.neighborhood = Neighborhood.objects.get(id=1)
        self.neighborhood.neighborhood_name = 'new name'
        self.neighborhood.update_neighborhood()
        self.updated_neighborhood = Neighborhood.objects.get(id=1)
        self.assertEqual(self.updated_neighborhood.name,'new name')

    def test_update_occupants(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.neighborhood = Neighborhood.objects.get(id=1)
        self.neighborhood.update_occupants()
        self.updated_neighborhood = Neighborhood.objects.get(id=1)
        self.assertTrue(self.updated_neighborhood.occupants == 2)