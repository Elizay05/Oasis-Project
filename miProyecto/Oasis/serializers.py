from .models import *

from rest_framework import serializers


# Serializers define the API representation.
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'clave', 'cedula', 'fecha_nacimiento', 'rol', 'estado', 'foto']

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha', 'hora_incio', 'descripcion', 'foto']

class MesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mesa
        fields = ['id', 'usuario', 'estado', 'codigo_qr']

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'evento', 'mesa', 'fecha_compra', 'hora_compra', 'codigo_qr']

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'foto']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'foto', 'categoria', 'precio']

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'producto', 'detalles', 'estado', 'precio']

class PedidoMesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PedidoMesa
        fields = ['id', 'mesa', 'producto', 'cantidad']

"""class InventarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'cantidad', 'fecha_caducidad']"""

class GaleriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galeria
        fields = ['id', 'nombre', 'fecha', 'foto']

class FotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fotos
        fields = ['id', 'foto', 'carpeta']

class VentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venta
        fields = ['fecha_venta', 'usuario', 'estado']

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'cantidad', 'precio_historico']