# Generated by Django 5.0.4 on 2024-06-19 23:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios', '0005_servicio_descripcion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=16)),
                ('fecha_vencimiento', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pagoservicio',
            name='tarjeta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_servicios.tarjeta'),
        ),
    ]
