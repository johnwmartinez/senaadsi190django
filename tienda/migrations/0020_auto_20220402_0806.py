# Generated by Django 3.2.8 on 2022-04-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0019_clientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Orden_ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.TextField()),
                ('session_id', models.TextField()),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.clientes')),
            ],
        ),
    ]