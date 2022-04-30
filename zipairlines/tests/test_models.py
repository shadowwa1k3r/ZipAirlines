from django.test import TestCase
from ..models import Airplane


class AirplaneTest(TestCase):
    """ Test module for Airplane model """

    def setUp(self):
        Airplane.objects.create(airplane_id=3, passenger_count=100)
        Airplane.objects.create(airplane_id=12, passenger_count=200)

    def test_airplane(self):
        """ Test if calculating airplane fuel value working """
        
        airplane1 = Airplane.objects.get(airplane_id=3)
        airplane2 = Airplane.objects.get(airplane_id=12)
        self.assertEqual(airplane1.fuel_tank, airplane1.airplane_id*200)
        self.assertEqual(airplane2.fuel_tank, airplane2.airplane_id*200)