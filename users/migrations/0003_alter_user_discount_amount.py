# Generated by Django 5.0.7 on 2024-12-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='discount_amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
