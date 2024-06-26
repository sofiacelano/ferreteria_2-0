# Generated by Django 5.0.4 on 2024-06-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoCatalogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen_principal', models.ImageField(upload_to='imagenes/')),
                ('imagen_extra1', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('imagen_extra2', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('imagen_extra3', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
    ]
