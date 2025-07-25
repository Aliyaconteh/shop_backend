# Generated by Django 5.2.3 on 2025-07-15 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_purchase_purchaseitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='customer_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='PurchaseItem',
        ),
    ]
