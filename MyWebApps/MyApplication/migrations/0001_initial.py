# Generated by Django 5.0.6 on 2024-06-08 21:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('phone', models.IntegerField(blank=True, null=True, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name', 'address'],
            },
        ),
    ]