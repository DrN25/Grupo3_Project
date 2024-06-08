from django.contrib import admin

from .models.Usuario import Usuario
from .models.Vendedor import Vendedor
from .models.Categoria import Categoria
from .models.Producto import Producto
from .models.Comentario import Comentario
from .models.Publicacion import Publicacion
from .models.CarritoCompras import CarritoCompras
from .models.ProductoPedido import ProductoPedido
from .models.Pedido import Pedido

admin.site.register(Usuario)
admin.site.register(Vendedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Publicacion)
admin.site.register(CarritoCompras)
admin.site.register(ProductoPedido)
admin.site.register(Pedido)
