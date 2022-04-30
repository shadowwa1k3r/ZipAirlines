import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.utils.http import urlencode
from ..models import Airplane
from ..api.airplane.serializers import AirplaneCreateSerializer, AirplaneListDetailSerializer

client = Client()


class GetAirPlanesTest(TestCase):

    def setUp(self):
        self.airplane1 = Airplane.objects.create(airplane_id=3, passenger_count=100)
        self.airplane2 = Airplane.objects.create(airplane_id=12, passenger_count=200)

    def test_get_all_airplanes(self):
        response = client.get(reverse('get_all_airplanes'))
        airplanes = Airplane.objects.all()
        serializer = AirplaneListDetailSerializer(airplanes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_one_airplane_test(self):
        response = client.get(reverse('get_all_airplanes')+'?'+urlencode({'airplane_id':3}))
        airplane = Airplane.objects.filter(airplane_id=3)
        serializer = AirplaneListDetailSerializer(airplane, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateAirplanesTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'airplane_id': 4,
            'passenger_count': 250,
        }
        self.invalid_data = {
            'airplane_id': 'five',
            'passenger_count': 'fouryfive',
        }


    def test_create_valid_airplane(self):
        response = client.post(
            reverse('create_airplane'),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_airplane(self):
        response = client.post(
            reverse('create_airplane'),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
