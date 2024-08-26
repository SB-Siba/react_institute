# Generated by Django 5.0.7 on 2024-08-26 05:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('products', models.JSONField(blank=True, default=dict, null=True)),
                ('coupon', models.CharField(blank=True, max_length=255, null=True)),
                ('order_value', models.FloatField(default=0.0)),
                ('order_meta_data', models.JSONField(blank=True, default=dict, null=True)),
                ('order_status', models.CharField(choices=[('Placed', 'Placed'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('On_Way', 'On_Way'), ('Refund', 'Refund'), ('Return', 'Return')], default='Placed', max_length=255)),
                ('razorpay_payment_id', models.TextField(blank=True, null=True)),
                ('razorpay_order_id', models.TextField(blank=True, null=True)),
                ('razorpay_signature', models.TextField(blank=True, null=True)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Refunded', 'Refunded')], default='Paid', max_length=255)),
                ('payment_method', models.CharField(choices=[('razorpay', 'Razorpay'), ('cod', 'Cash on Delivery')], default='razorpay', max_length=10)),
                ('address', models.JSONField(blank=True, default=dict, null=True)),
                ('transaction_id', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('can_edit', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
