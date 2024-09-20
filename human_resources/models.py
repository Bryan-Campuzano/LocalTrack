from django.db import models

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    fecha = models.DateField()
    empleado_id = models.IntegerField()

    def __str__(self):
        return f'Asistencia {self.id_asistencia}'
    
class Nomina(models.Model):
    id_nomina = models.AutoField(primary_key=True)
    empleado_id = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    def __str__(self):
        return f'Nómina {self.id_nomina}'

class Pqrs(models.Model):
    idPqrs = models.AutoField(primary_key=True)  # Campo auto-incremental
    asunto = models.CharField(max_length=500)  # Asunto del PQRS
    fechaRadicado = models.DateField()  # Fecha en la que se radica el PQRS
    contenidoPqrs = models.CharField(max_length=500)  # Contenido del PQRS
    fkCliente = models.IntegerField()  # Llave foránea (asumiendo que está relacionada con otra tabla de Cliente)

    def __str__(self):
        return f"{self.asunto} - {self.fechaRadicado}"
    
class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

