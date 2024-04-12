# Generated by Django 5.0.3 on 2024-04-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0019_evento_precio_entrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='usuario',
        ),
        migrations.AddField(
            model_name='mesa',
            name='estado_reserva',
            field=models.CharField(choices=[('Reservada', 'Reservada'), ('Disponible', 'Disponible')], default='Reservada', max_length=10),
        ),
        migrations.AddField(
            model_name='mesa',
            name='nombre',
            field=models.CharField(default='mesa', max_length=300),
        ),
    ]
