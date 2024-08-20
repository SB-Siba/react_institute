# Generated by Django 5.0.7 on 2024-08-17 06:25

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_simpleproduct_delivery_charge_per_bag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleproduct',
            name='cgst_rate',
        ),
        migrations.RemoveField(
            model_name='simpleproduct',
            name='sgst_rate',
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='gst_rate',
            field=models.DecimalField(decimal_places=3, default=Decimal('0.03'), max_digits=5),
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='taxable_value',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), editable=False, max_digits=10),
        ),
    ]
