# Generated by Django 5.0.4 on 2024-06-19 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios', '0006_tarjeta_pagoservicio_tarjeta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='cliente',
        ),
    ]
