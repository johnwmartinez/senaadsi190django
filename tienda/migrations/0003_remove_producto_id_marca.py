# Generated by Django 3.2.8 on 2022-04-01 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_id_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_marca',
        ),
    ]