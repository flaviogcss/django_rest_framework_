# Generated by Django 3.0.2 on 2020-01-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20200122_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='forma_pagamento',
            field=models.CharField(choices=[('BOLETO', 'Boleto'), ('CARTAO', 'Cartão'), ('DINHEIRO', 'Dinheiro'), ('', '')], max_length=50),
        ),
    ]