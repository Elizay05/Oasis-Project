# Generated by Django 4.2.7 on 2023-11-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(default='No_Image', upload_to='fotos/')),
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
                ('foto', models.ImageField(default='No_Image', upload_to='fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(default='No_Image', upload_to='fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Activa', 'Activa'), ('Disponible', 'Disponible')], max_length=10)),
                ('codigo_qr', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('clave', models.CharField(max_length=254)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('rol', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Bartender'), (3, 'Mesero'), (4, 'Cliente')], default=4)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Bloqueado', 'Bloqueado')], max_length=9)),
                ('foto', models.ImageField(upload_to='fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('hora_compra', models.TimeField()),
                ('codigo_qr', models.CharField(max_length=100, unique=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.evento')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(default='No_image', upload_to='fotos/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoMesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.TextField()),
                ('estado', models.CharField(choices=[('En preparación', 'En preparacion'), ('Entregado', 'Entregado'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], max_length=14)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
            ],
        ),
        migrations.AddField(
            model_name='mesa',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.usuario'),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_caducidad', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(default='No_Image', upload_to='fotos/')),
                ('carpeta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.galeria')),
            ],
        ),
    ]
