# Generated by Django 4.2.7 on 2023-11-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(default='No_image', upload_to='fotos/'),
        ),
    ]