# Generated by Django 5.0.4 on 2024-06-05 23:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mis_productos", "0012_remove_producto_visible_producto_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="visible",
            field=models.BooleanField(default=True),
        ),
    ]
