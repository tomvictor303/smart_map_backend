from django.db import models

class Technician(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70,blank=False, default='')
    lat = models.DecimalField(max_digits=20, decimal_places=14, blank=False, default=0)
    lon = models.DecimalField(max_digits=20, decimal_places=14, blank=False, default=0)
