# Generated by Django 5.0.6 on 2024-06-08 22:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0008_publicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('idCarrito', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('1', 'empty'), ('2', 'in process'), ('3', 'completed')], default='1', max_length=1)),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApplication.producto')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApplication.usuario')),
            ],
            options={
                'ordering': ['status', 'idUsuario', 'idProducto'],
            },
        ),
    ]