# Generated by Django 5.0.3 on 2024-04-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0020_remove_mesa_usuario_mesa_estado_reserva_mesa_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='estado_reserva',
            field=models.CharField(choices=[('Reservada', 'Reservada'), ('Disponible', 'Disponible')], default='Disponible', max_length=10),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='nombre',
            field=models.CharField(max_length=300),
        ),
    ]
