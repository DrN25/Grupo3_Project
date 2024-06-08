from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Producto import Producto

class ProductoPedido(models.Model):
    idPedido = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.IntegerField(null=False, blank=False)
    total = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2, default=0.00)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idProducto', 'amount', 'total']

    def save(self, *args, **kwargs):
        return super(ProductoPedido, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.idProducto, self.amount, self.total)