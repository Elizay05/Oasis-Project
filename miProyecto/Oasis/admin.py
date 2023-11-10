from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','cedula','fecha_nacimiento','email','telefono','rol','estado']
    search_fields = ['id','nombre','cedula','email','telefono','rol','estado']
    list_filter = ['rol']
    list_editable = ['estado']

class EventoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','fecha','hora_incio','descripcion']
    search_fields = ['id','nombre','fecha','hora_incio']
    list_filter = ['fecha']
    list_editable = ['nombre','fecha','hora_incio']

class MesaAdmin(admin.ModelAdmin):
    list_display = ['id','estado','codigo_qr']
    search_fields = ['id','estado']
    list_filter = ['estado']
    list_editable = ['estado']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','evento','mesa','fecha_compra','hora_compra','codigo_qr']
    search_fields =['id','usuario','evento','mesa','fecha_compra']
    list_filter = ['evento','fecha_compra']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion']
    search_fields = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','imagen','categoria', 'precio']
    search_fields = ['id','nombre','categoria', 'precio']
    list_filter = ['categoria']
    list_editable = ['precio']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','mesa','producto','detalles','estado','precio']
    search_fields = ['id','mesa','estado']
    list_filter = ['estado']
    list_editable = ['estado']

class PedidoMesaAdmin(admin.ModelAdmin):
    list_display = ['id','mesa','producto','cantidad'] 
    search_fields = ['id','mesa','producto','cantidad']
    list_filter = ['mesa']

class InventarioAdmin(admin.ModelAdmin):
    list_display = ['id','producto','cantidad','fecha_caducidad']
    search_fields = ['id','producto','cantidad','fecha_caducidad']
    list_filter = ['fecha_caducidad']
    list_editable = ['cantidad','fecha_caducidad']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(PedidoMesa, PedidoMesaAdmin)