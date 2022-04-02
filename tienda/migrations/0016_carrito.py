# Generated by Django 3.2.8 on 2022-04-02 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0015_alter_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.TextField(blank=True, null=True)),
                ('precio', models.FloatField()),
                ('producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]
