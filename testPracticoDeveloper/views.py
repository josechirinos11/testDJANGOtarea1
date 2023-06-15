import requests
from django.http import JsonResponse
from django.db import IntegrityError
from .models import BikeNetwork
from django.shortcuts import render
def bike_network_info(request):
    # Obtén la instancia de BikeNetwork que deseas mostrar en la vista
    bike_network = BikeNetwork.objects.first()  # Puedes ajustar esta consulta según tus necesidades

    # Renderiza la plantilla con la instancia de BikeNetwork como contexto
    return render(request, 'bike_network_info.html', {'bike_network': bike_network})

def obtener_datos_api(request):
    url = 'https://api.citybik.es/v2/networks/bikerio'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        # Guardar los datos en la base de datos
        bike_network_data = data['network']
        network_id = bike_network_data['id']
        try:
            # Intentar crear una nueva instancia
            bike_network = BikeNetwork.objects.create(
                name=bike_network_data['name'],
                gbfs_href=bike_network_data['gbfs_href'],
                href=bike_network_data['href'],
                network_id=network_id,
                company=bike_network_data['company'],
                location=bike_network_data['location'],
                stations=bike_network_data['stations']
            )
            return JsonResponse({'message': 'Los datos han sido guardados correctamente.', 'data': bike_network_data}, json_dumps_params={'indent': 4})
        except IntegrityError:
            # Si ya existe una instancia con el mismo network_id, actualizarla en su lugar
            bike_network = BikeNetwork.objects.get(network_id=network_id)
            bike_network.name = bike_network_data['name']
            bike_network.gbfs_href = bike_network_data['gbfs_href']
            bike_network.href = bike_network_data['href']
            bike_network.company = bike_network_data['company']
            bike_network.location = bike_network_data['location']
            bike_network.stations = bike_network_data['stations']
            bike_network.save()
            return JsonResponse({'message': 'Los datos han sido actualizados correctamente.', 'data': bike_network_data}, json_dumps_params={'indent': 4})
    else:
        return JsonResponse({'error': 'Error al obtener los datos de la API'}, status=500, json_dumps_params={'indent': 4})
