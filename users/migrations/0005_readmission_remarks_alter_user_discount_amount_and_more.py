# Generated by Django 5.1 on 2024-11-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_readmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='readmission',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='discount_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fees_received',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
