# Generated by Django 3.2.8 on 2022-04-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_remove_producto_id_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_marca',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
