from django.contrib import admin

from .models.Usuario import Usuario
from .models.Vendedor import Vendedor
from .models.Categoria import Categoria
from .models.Producto import Producto

admin.site.register(Usuario)
admin.site.register(Vendedor)
admin.site.register(Categoria)
admin.site.register(Producto)
