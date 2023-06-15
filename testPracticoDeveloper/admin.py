from django.contrib import admin
from .models import BikeNetwork

@admin.register(BikeNetwork)
class BikeNetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'network_id', 'location']  # Campos que se mostrarán en la lista de objetos
    search_fields = ['name', 'network_id']  # Campos por los que se puede buscar
    readonly_fields = ['name', 'network_id', 'gbfs_href', 'href', 'company', 'location', 'stations']  # Campos de solo lectura


