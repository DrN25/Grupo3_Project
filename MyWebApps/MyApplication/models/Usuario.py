from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Usuario(models.Model):
    idUsuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True, max_length=255)
    phone = models.IntegerField(unique=True, null=True, blank=True)
    password = models.CharField(null=False, blank=False, max_length=255)
    address = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.name)