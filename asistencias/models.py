from django.db import models

class Asistencia(models.Model):
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    tipo_documento = models.CharField(max_length = 30)
    documento = models.CharField(max_length = 100)
    whatsapp = models.CharField(max_length = 100)
    fecha = models.DateField()
    asistio = models.BooleanField()
    
    def __str__(self):
        return self.nombres