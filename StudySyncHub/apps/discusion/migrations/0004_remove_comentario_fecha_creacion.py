# Generated by Django 4.2.7 on 2023-11-30 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discusion', '0003_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha_creacion',
        ),
    ]
