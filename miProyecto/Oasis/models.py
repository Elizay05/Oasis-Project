from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    clave = models.CharField(max_length=254)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    ROLES = (
        (1, "Administrador"),
        (2, "Bartender"),
        (3, "Mesero"),
        (4, "Cliente"),
    )
    rol = models.IntegerField(choices=ROLES, default=4)
    ESTADO = (
        (1, "Activo"),
        (2, "Bloqueado"),
    )
    estado = models.IntegerField(choices=ESTADO, default=1)
    foto = models.ImageField(upload_to="Img_usuarios/", default="Img_usuarios/default.png")

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    fecha = models.DateField()
    hora_incio = models.TimeField() 
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="Img_eventos/", default="Img_eventos/default.png")

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    ACTIVA = 'Activa'
    DISPONIBLE = 'Disponible'

    ESTADO_CHOICES = (
        (ACTIVA, 'Activa'),
        (DISPONIBLE, 'Disponible'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    codigo_qr = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.id}'

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    fecha_compra = models.DateField()
    hora_compra = models.TimeField()
    codigo_qr = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Mesa: {self.mesa} - Evento: {self.evento.nombre}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="Img_categorias/", default="Img_categorias/default.png")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="Img_productos/", default="Img_productos/default.png")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    detalles = models.TextField()
    PREPARACION = 'En preparación'
    ENTREGADO = 'Entregado'
    PAGADO = 'Pagado'
    CANCELADO = 'Cancelado'

    ESTADO_CHOICES = (
        (PREPARACION, 'En preparacion'),
        (ENTREGADO, 'Entregado'),
        (PAGADO, 'Pagado'),
        (CANCELADO, 'Cancelado'),
    )

    estado = models.CharField(max_length=14, choices=ESTADO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Mesa {self.mesa.id}'


class PedidoMesa(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    fecha_caducidad = models.DateField()

    def __str__(self):
        return self.producto.nombre

class Galeria(models.Model):
    nombre = models.CharField(max_length=254)
    fecha = models.DateField()
    foto = models.ImageField(upload_to="Img_carpeta/", default="Img_carpeta/default.png")


class Fotos(models.Model):
    foto = models.ImageField(upload_to="Img_galeria/", default="Img_galeria/default.png")
    carpeta = models.ForeignKey(Galeria, on_delete=models.DO_NOTHING)
