from django.db import models
from django.utils import timezone

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    created_on = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='productos')

    def __str__(self):
        return self.nombre
