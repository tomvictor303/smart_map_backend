from django.db import models

# Create your models here.
class Plan(models.Model):
    task = models.CharField(max_length=255, blank=False, default='')
    person = models.IntegerField(blank=False, default=0)
    date = models.DateField()

class PlanPriority(models.Model):    
    priorities = models.TextField()
    person = models.IntegerField(blank=False, default=0)
    date = models.DateField()