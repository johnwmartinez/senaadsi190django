# Generated by Django 3.2.8 on 2022-04-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_rename_suit_producto_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
