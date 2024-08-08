# Generated by Django 5.0.7 on 2024-08-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='user_profile_pic/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('address', models.JSONField(blank=True, default=dict, null=True)),
                ('deletion_requested', models.BooleanField(default=False)),
                ('deletion_date', models.DateTimeField(blank=True, null=True)),
                ('wallet', models.FloatField(default=0.0)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('meta_data', models.JSONField(default=dict)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
