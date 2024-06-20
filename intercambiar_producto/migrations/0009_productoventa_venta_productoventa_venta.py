# Generated by Django 5.0.4 on 2024-06-19 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_remove_venta_productos_delete_productoventa_and_more'),
        ('intercambiar_producto', '0008_intercambio_venta_realizada'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.productocatalogo')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productos', models.ManyToManyField(through='intercambiar_producto.ProductoVenta', to='catalogo.productocatalogo')),
            ],
        ),
        migrations.AddField(
            model_name='productoventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intercambiar_producto.venta'),
        ),
    ]