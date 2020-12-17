from django.db import models
from portafolio.cliente.models import *
from portafolio.receta.models import *
from django.utils.timezone import now
# Create your models here.

class Carrito(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    
    class Meta:
        db_table = 'Carrito'
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    estado = models.CharField(max_length=50)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    tiempo = models.IntegerField()

    class Meta:
        db_table = 'Pedido'

class Orden_Compra(models.Model):
    total = models.IntegerField()
    fecha = models.DateTimeField(default=now,blank=True)
    num_factura = models.IntegerField()
    id_pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Orden_Compra'
        unique_together = (("num_factura","id_pedido"),)

class Menu(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Menu'
    
    def __str__(self):
        return self.nombre


