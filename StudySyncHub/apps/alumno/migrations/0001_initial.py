# Generated by Django 4.2.7 on 2023-11-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=30)),
                ('apellido', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]