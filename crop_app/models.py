# models.py
from django.db import models

class CropInput(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    
    def __str__(self):
        return f"Crop Input {self.id}"

# Create your models here.
