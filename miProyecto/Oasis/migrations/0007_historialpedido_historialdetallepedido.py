# Generated by Django 5.0.3 on 2024-05-22 14:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0006_rename_detalles_pedido_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('comentario', models.TextField(default='')),
                ('estado', models.CharField(max_length=14)),
                ('total', models.IntegerField()),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.mesa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialDetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Oasis.producto')),
                ('historial_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oasis.historialpedido')),
            ],
        ),
    ]
