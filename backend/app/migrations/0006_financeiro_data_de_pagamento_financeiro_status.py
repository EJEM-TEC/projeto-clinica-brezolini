# Generated by Django 5.1 on 2024-10-09 22:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_financeiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro',
            name='data_de_pagamento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='financeiro',
            name='status',
            field=models.CharField(default='Pendente', max_length=20),
        ),
    ]
