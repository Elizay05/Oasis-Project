# Generated by Django 5.0.1 on 2024-02-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0012_delete_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Activo'), (1, 'Bloqueado')], default=1),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
