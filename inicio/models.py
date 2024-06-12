from django.db import models

# Create your models here.
class Auto(models.Model):
    modelo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    
    def __str__(self):
        return f'Soy el auto {self.marca} {self.modelo}'