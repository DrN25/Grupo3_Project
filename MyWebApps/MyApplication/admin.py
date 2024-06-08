from django.contrib import admin

from .models.Usuario import Usuario
from .models.Vendedor import Vendedor
from .models.Categoria import Categoria

admin.site.register(Usuario)
admin.site.register(Vendedor)
admin.site.register(Categoria)
