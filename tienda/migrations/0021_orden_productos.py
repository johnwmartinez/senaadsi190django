# Generated by Django 3.2.8 on 2022-04-02 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_auto_20220402_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.TextField()),
                ('cantidad', models.TextField()),
                ('subtotal', models.TextField()),
                ('orden', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.orden_ventas')),
                ('producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]