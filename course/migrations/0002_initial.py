# Generated by Django 5.1 on 2024-11-13 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.batch'),
        ),
        migrations.AddField(
            model_name='examresult',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to='course.course'),
        ),
    ]
