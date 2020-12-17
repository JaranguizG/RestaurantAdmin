from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=125)
    telefono = models.IntegerField()
    

    class Meta:
        db_table = 'Cliente'
    
    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    ESTADO = (
        ('disponible', 'DISPONIBLE'),
        ('ocupada','OCUPADA'),

    )
    num_persona = models.IntegerField()
    estado = models.CharField(choices=ESTADO, max_length=30,null=True)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'Mesa'
    
    def __str__(self):
        return self.estado
