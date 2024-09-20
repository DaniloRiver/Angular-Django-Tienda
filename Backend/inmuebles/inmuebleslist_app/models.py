from django.db import models # type: ignore

class Inmueble(models.Model):
    _direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    imagen  =models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self._direccion
