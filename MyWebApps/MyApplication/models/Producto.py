from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Categoria import Categoria
from .Vendedor import Vendedor

class Producto(models.Model):
    idProducto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    weight = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    unitPrice = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    stock = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='image_photos/', null=True, blank=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    idVendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', 'unitPrice', 'stock', 'idCategoria', 'idVendedor']

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s" % (self.name, self.unitPrice, self.stock, self.idCategoria, self.idVendedor)