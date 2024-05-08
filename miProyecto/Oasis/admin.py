from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','cedula','fecha_nacimiento','email','password','rol','estado','foto','last_login']
    search_fields = ['id','nombre','cedula','email','telefono','rol','estado']
    list_filter = ['rol']
    list_editable = ['estado']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'nombre_plural', 'fecha', 'hora_incio', 'descripcion', 'aforo', 'precio_entrada', 'precio_vip' , 'foto']
    search_fields = ['id','nombre','fecha','hora_incio']
    list_filter = ['fecha']
    list_editable = ['nombre','fecha','hora_incio']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")

    def nombre_plural(self, obj):
        return mark_safe(f"<span style='color:red'>{obj.nombre}'s<span>")


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'capacidad', 'estado','estado_reserva','codigo_qr']
    search_fields = ['id','estado', 'capacidad','estado_reserva']
    list_filter = ['estado', 'capacidad','estado_reserva']
    list_editable = ['estado', 'capacidad', 'estado_reserva']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    #Agregar 'usuario' cuando funcione
    list_display = ['id','evento','mesa','fecha_compra','hora_compra','codigo_qr']
    search_fields =['id','usuario','evento','mesa','fecha_compra']
    list_filter = ['evento','fecha_compra']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion', 'foto']
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','inventario','precio','ver_foto']
    search_fields = ['id','nombre', 'precio']
    list_editable = ['precio']

    def ver_foto(self, obj):
        if obj.foto:
            return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='15%'></a>")
        

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','mesa','producto','detalles','estado','precio']
    search_fields = ['id','mesa','estado']
    list_filter = ['estado']
    list_editable = ['estado']

@admin.register(PedidoMesa)
class PedidoMesaAdmin(admin.ModelAdmin):
    list_display = ['id','mesa','producto','cantidad'] 
    search_fields = ['id','mesa','producto','cantidad']
    list_filter = ['mesa']

"""@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['id','producto','cantidad','fecha_caducidad']
    search_fields = ['id','producto','cantidad','fecha_caducidad']
    list_filter = ['fecha_caducidad']
    list_editable = ['cantidad','fecha_caducidad']"""


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'foto', 'ver_foto']
    search_fields = ['nombre', 'fecha', 'foto']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")

@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
    list_display = ['foto', 'carpeta', 'ver_foto']
    search_fields = ['foto', 'carpeta']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    #Agregar 'usuario' cuando funcione
    list_display = ['id', 'fecha_venta']

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'venta', 'producto', 'cantidad', 'precio_historico', 'subtotal']

    def subtotal(self, obj):
        return f"{obj.cantidad * obj.precio_historico}"