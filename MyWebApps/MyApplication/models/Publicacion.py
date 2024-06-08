from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Producto import Producto
from .Vendedor import Vendedor
from .Comentario import Comentario

class Publicacion(models.Model):
    idPublicacion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    likes = models.IntegerField(null=False, blank=False, default=0)
    dislikes = models.IntegerField(null=False, blank=False, default=0)
    idVendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idComentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idProducto', 'idVendedor']

    def save(self, *args, **kwargs):
        return super(Publicacion, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.idProducto)