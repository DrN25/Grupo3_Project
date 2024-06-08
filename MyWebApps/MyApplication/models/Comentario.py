from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from .Usuario import Usuario

class Comentario(models.Model):
    idComentario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(null=False, blank=False, max_length=255)
    date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idUsuario', 'content']

    def save(self, *args, **kwargs):
        self.content = self.content.upper()
        return super(Comentario, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.idUsuario, self.date)