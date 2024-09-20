from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Inventario {self.id_inventario}'

class Devolucion(models.Model):
    id_devolucion = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=100)
    fecha = models.DateField()
    venta_id = models.IntegerField()

    def __str__(self):
        return f'Devolución {self.id_devolucion}'
    
class Remision(models.Model):
    id_remision = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente_id = models.IntegerField()
    venta_id = models.IntegerField()

    def __str__(self):
        return f'Remision {self.id_remision}'

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return self.descripcion
