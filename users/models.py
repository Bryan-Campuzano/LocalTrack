from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class RolPermiso(models.Model):
    id_rol_permisos = models.AutoField(primary_key=True)
    rol_id = models.IntegerField()
    permiso_id = models.IntegerField()
    
class UsuarioRol(models.Model):
    id_usuario_rol = models.AutoField(primary_key=True)
    usuario_id = models.IntegerField()
    rol_id = models.IntegerField()

