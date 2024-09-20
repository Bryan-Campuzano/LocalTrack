from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha_emision = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Factura {self.id_factura}'
    
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente_id = models.IntegerField()

    def __str__(self):
        return f'Venta {self.id_venta}'

class Descuento(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f'Descuento {self.porcentaje}%'
    
class Pyme(models.Model):
    id_pyme = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

