# Generated by Django 5.0.4 on 2024-06-19 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_productoventa_venta_productoventa_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='productos',
        ),
        migrations.DeleteModel(
            name='ProductoVenta',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
