# Generated by Django 5.1 on 2024-10-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_financeiro_parcelas'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro',
            name='numero_parcela',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='financeiro',
            name='parcelas',
            field=models.PositiveIntegerField(),
        ),
    ]
