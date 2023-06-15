import requests
from django.http import JsonResponse

def obtener_datos_api(request):
    url = 'https://api.citybik.es/v2/networks/bikerio'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, json_dumps_params={'indent': 4})
    else:
        return JsonResponse({'error': 'Error al obtener los datos de la API'}, status=500)
















import requests
from django.http import JsonResponse
from .models import BikeNetwork, Location, BikeStation
from datetime import datetime

def obtener_datos_api(request):
    url = 'https://api.citybik.es/v2/networks/bikerio'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Guardar los datos en la base de datos
        
        network_data = data['network']
        location_data = network_data['location']
        stations_data = network_data['stations']
        
        # Crear una instancia de BikeNetwork
        bike_network = BikeNetwork.objects.create(
            company=network_data['company'],
            gbfs_href=network_data['gbfs_href'],
            href=network_data['href'],
            id=network_data['id'],
            location=network_data['location'],
            name=network_data['name'],
            stations=network_data['stations'],
        )
        
        # Crear una instancia de Location asociada a BikeNetwork
        company = Location.objects.create(
            bike_network=bike_network,
            city=location_data['city'],
            country=location_data['country'],
            latitude=location_data['latitude'],
            longitude=location_data['longitude']
        )
        
         # Crear una instancia de Location asociada a BikeNetwork
        location = Location.objects.create(
            bike_network=bike_network,
            city=location_data['city'],
            country=location_data['country'],
            latitude=location_data['latitude'],
            longitude=location_data['longitude']
        )
        # Crear instancias de BikeStation asociadas a BikeNetwork
        for station_data in stations_data:
            station = BikeStation.objects.create(
                bike_network=bike_network,
                empty_slots=station_data['empty_slots'],
                free_bikes=station_data['free_bikes'],
                station_id=station_data['id'],
                latitude=station_data['latitude'],
                longitude=station_data['longitude'],
                name=station_data['name'],
                timestamp=datetime.strptime(station_data['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
            )
        
        return JsonResponse(data, json_dumps_params={'indent': 4})
    else:
        return JsonResponse({'error': 'Error al obtener los datos de la API'}, status=500)












#                    modelllllllllllllllllllllllllllllllllllllllllllllllll

from django.db import models


class BikeNetwork(models.Model):
    name = models.CharField(max_length=100)
    gbfs_href = models.URLField()
    href = models.CharField(max_length=100)
    network_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    bike_network = models.OneToOneField(BikeNetwork, on_delete=models.CASCADE, related_name='location')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.city}, {self.country}"

class BikeStation(models.Model):
    bike_network = models.ForeignKey(BikeNetwork, on_delete=models.CASCADE, related_name='stations')
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    station_id = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name



