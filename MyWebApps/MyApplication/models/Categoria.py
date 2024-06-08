from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Categoria(models.Model):
    idCategoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name)