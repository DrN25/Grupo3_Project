# Generated by Django 5.0.6 on 2024-06-08 21:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0002_vendedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]