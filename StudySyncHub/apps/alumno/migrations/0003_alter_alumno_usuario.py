# Generated by Django 4.2.7 on 2023-11-17 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
        ('alumno', '0002_alumno_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to='custom_user.customuser'),
        ),
    ]
