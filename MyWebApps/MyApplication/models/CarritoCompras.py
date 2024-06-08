from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Usuario import Usuario
from .Producto import Producto

class CarritoCompras(models.Model):
    idCarrito = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2, default=0)
    STATUS = [
        ('empty','empty'),
        ('in_process','in process'),
        ('completed','completed')
    ]
    status = models.CharField(null=False, max_length=10, choices=STATUS, default='empty')
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['status', 'idUsuario', 'idProducto']

    def save(self, *args, **kwargs):
        self.status = self.status.upper()
        return super(CarritoCompras, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.status, self.idUsuario, self.idProducto)