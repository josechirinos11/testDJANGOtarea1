from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

class BikeNetwork(models.Model):
    name = models.CharField(max_length=100)
    gbfs_href = models.URLField()
    href = models.CharField(max_length=100)
    network_id = models.CharField(max_length=100, unique=True)
    company = ArrayField(models.CharField(max_length=100), default=list)
    location = models.JSONField()
    stations = models.JSONField()

    def __str__(self):
        return self.name
