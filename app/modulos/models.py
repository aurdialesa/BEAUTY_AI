from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password
class Empleado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    identificacion = models.CharField(max_length=50, unique= True,verbose_name='Identificación')
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='img', null=True, blank=True)
    contrasena = models.CharField(max_length=128, default='')

    def save(self, *args, **kwargs):
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    db_table = 'empleado'
    ordering = ['id']


