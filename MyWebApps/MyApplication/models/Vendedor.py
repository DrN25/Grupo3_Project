from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Vendedor(models.Model):
    idVendedor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True, max_length=255)
    phone = models.IntegerField(unique=True, null=True, blank=True)
    password = models.CharField(null=False, blank=False, max_length=255)
    address = models.CharField(null=False, blank=False, max_length=255)
    description = models.CharField(null=False, blank=False, max_length=255)
    perfilPhoto = models.ImageField(upload_to='perfil_photos/', null=True, blank=True)

    class Meta:
        ordering = ['name', 'address']

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Vendedor, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.name, self.address)