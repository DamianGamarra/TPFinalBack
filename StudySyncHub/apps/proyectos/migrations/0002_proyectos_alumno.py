# Generated by Django 4.2.7 on 2023-11-28 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_alter_alumno_usuario'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='alumno.alumno'),
        ),
    ]
