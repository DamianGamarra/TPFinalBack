# Generated by Django 4.2.7 on 2023-11-17 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to='custom_user.customuser'),
        ),
    ]
