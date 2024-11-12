# Generated by Django 5.1.1 on 2024-11-05 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_alter_exam_options_exam_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='student_photos/')),
                ('course_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theory_mark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('practical_mark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grade', models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=2)),
                ('result', models.CharField(choices=[('passed', 'Passed'), ('failed', 'Failed')], max_length=7)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.student')),
            ],
        ),
    ]
