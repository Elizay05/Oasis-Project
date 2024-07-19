# Generated by Django 5.0.3 on 2024-07-19 14:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(default='Img_categorias/default.png', upload_to='Img_categorias/')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('hora_incio', models.TimeField()),
                ('descripcion', models.TextField()),
                ('aforo', models.IntegerField(default=500)),
                ('entradas_disponibles', models.IntegerField(default=500)),
                ('precio_entrada', models.IntegerField(default=50000)),
                ('precio_vip', models.IntegerField(default=75000)),
                ('reservas', models.BooleanField(default=False)),
                ('foto', models.ImageField(default='Img_eventos/default.png', upload_to='Img_eventos/')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(default='Img_carpeta/default.png', upload_to='Img_carpeta/')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('capacidad', models.IntegerField(default=5)),
                ('precio', models.IntegerField(default=1000000)),
                ('estado', models.CharField(choices=[('Activa', 'Activa'), ('Disponible', 'Disponible')], default='Disponible', max_length=10)),
                ('estado_reserva', models.CharField(choices=[('Reservada', 'Reservada'), ('Disponible', 'Disponible')], default='Disponible', max_length=10)),
                ('codigo_qr', models.CharField(max_length=100, unique=True)),
                ('usuario', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Enviado'), (3, 'Rechazada')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(default='Img_galeria/default.png', upload_to='Img_galeria/')),
                ('carpeta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.galeria')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('estado', models.CharField(choices=[('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='Pagado', max_length=14)),
                ('total', models.IntegerField()),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.TextField(default='')),
                ('estado', models.CharField(choices=[('En preparación', 'En preparacion'), ('Entregado', 'Entregado'), ('Cancelado', 'Cancelado')], default='En preparación', max_length=14)),
                ('total', models.IntegerField(default=0)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('inventario', models.IntegerField(default=0)),
                ('foto', models.ImageField(default='Img_productos/default.png', upload_to='Img_productos/')),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialDetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('historial_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oasis.historialpedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Eliminado', 'Eliminado')], default='Activo', max_length=10)),
                ('motivo_eliminacion', models.TextField(blank=True, default='')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oasis.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_historico', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('rol', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Bartender'), (3, 'Mesero'), (4, 'Cliente')], default=4)),
                ('estado', models.IntegerField(choices=[(1, 'Activo'), (2, 'Bloqueado')], default=1)),
                ('foto', models.ImageField(blank=True, default='Img_usuarios/default.png', upload_to='Img_usuarios/')),
                ('token_recuperar', models.CharField(blank=True, default='', max_length=254, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='venta',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField(default=0)),
                ('codigo_qr', models.CharField(max_length=100, unique=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.evento')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historialpedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CompraEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada_general', models.IntegerField(default=1)),
                ('entrada_vip', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=0)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oasis.evento')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
