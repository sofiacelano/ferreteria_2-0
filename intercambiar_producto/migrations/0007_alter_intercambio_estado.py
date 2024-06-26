# Generated by Django 5.0.4 on 2024-06-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambiar_producto', '0006_intercambio_fecha_alter_intercambio_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intercambio',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado'), ('ausente', 'Ausente')], default='pendiente', max_length=10),
        ),
    ]
