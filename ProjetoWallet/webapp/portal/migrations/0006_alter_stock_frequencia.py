# Generated by Django 4.0.6 on 2022-07-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_rename_exchange_stock_frequencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='frequencia',
            field=models.CharField(max_length=255, null='1m'),
        ),
    ]