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

class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='qwerty12345')
        self.business = Business(id=1,name='Test',user=self.user,neighborhood=self.neighborhood,email='test@test.com')
        self.neighborhood.save()
        self.business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.business.create_business()
        self.assertTrue(len(Business.objects.all()) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_find_business(self):
        self.business = Business.find_business(1)
        self.assertEqual(self.business.id, 1)

    def test_update_business(self):
        self.business = Business.find_business(1)
        self.business.name = 'Test name'
        self.business.update_business()
        self.updated_business = Business.find_business(1)
        self.assertEqual(self.updated_business.name, 'Test name')