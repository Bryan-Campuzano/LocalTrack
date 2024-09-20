from django.db import models

class Analisis(models.Model):
    id_analisis = models.AutoField(primary_key=True)
    kpi_nombre = models.CharField(max_length=45)
    kpi_valor = models.IntegerField()
    fecha = models.DateField()
    reporte = models.ForeignKey('Reporte', on_delete=models.CASCADE)

    def __str__(self):
        return self.kpi_nombre
    
class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    fecha = models.DateField()

    def __str__(self):
        return f'Reporte {self.id_reporte}'
    
class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion

