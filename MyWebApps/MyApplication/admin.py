from django.contrib import admin

from .models.Usuario import Usuario
from .models.Vendedor import Vendedor

admin.site.register(Usuario)
admin.site.register(Vendedor)
