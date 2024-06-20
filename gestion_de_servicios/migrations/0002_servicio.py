# Generated by Django 5.0.4 on 2024-06-12 04:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_servicios', '0001_initial'),
        ('gestion_de_sucursales', '0003_alter_perfilempleado_sucursal'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado'), ('publicado', 'Publicado')], default='pendiente', max_length=10)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_servicios.pagoservicio')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_sucursales.sucursal')),
            ],
        ),
    ]