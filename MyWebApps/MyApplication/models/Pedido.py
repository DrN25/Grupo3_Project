from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Usuario import Usuario
from .Vendedor import Vendedor
from .ProductoPedido import ProductoPedido

class Pedido(models.Model):
    idPedido = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    METODO_PAGO = [
        ('credito','Tarjeta de Credito'),
        ('debito','Tarjeta de Debito'),
        ('paypal','Paypal'),
        ('otro','Otros')
    ]
    payMethod = models.CharField(null=False, max_length=20, choices=METODO_PAGO, default='credito')
    total = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idVendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    idProductoPedido = models.ForeignKey(ProductoPedido, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idUsuario', 'idVendedor', 'idProductoPedido', 'total', 'date']

    def save(self, *args, **kwargs):
        self.payMethod = self.payMethod.upper()
        return super(Pedido, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.idUsuario, self.total)