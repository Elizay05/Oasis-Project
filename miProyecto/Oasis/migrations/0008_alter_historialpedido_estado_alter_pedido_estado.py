# Generated by Django 5.0.3 on 2024-05-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0007_historialpedido_historialdetallepedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialpedido',
            name='estado',
            field=models.CharField(choices=[('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='Pagado', max_length=14),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('En preparación', 'En preparacion'), ('Entregado', 'Entregado')], default='En preparación', max_length=14),
        ),
    ]
