# Generated by Django 5.0.7 on 2024-12-25 14:51

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('timing', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_students', models.PositiveIntegerField(blank=True, null=True)),
                ('total_seats', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CertificateDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('student_image', models.ImageField(blank=True, max_length=250, null=True, upload_to='student_photos/')),
                ('student_signature', models.ImageField(blank=True, max_length=250, null=True, upload_to='student_signatures/')),
                ('roll_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('abbreviation', models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.')], max_length=10)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('select_one', models.CharField(blank=True, choices=[('S/O', 'S/O'), ('D/O', 'D/O'), ('W/O', 'W/O')], max_length=10)),
                ('father_husband_name', models.CharField(blank=True, max_length=100)),
                ('show_father_husband_on_certificate', models.BooleanField(default=False)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('username', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('alternative_contact', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('pincode', models.CharField(blank=True, max_length=10)),
                ('permanent_address', models.TextField(blank=True)),
                ('aadhar_card_number', models.CharField(blank=True, max_length=12)),
                ('caste', models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC/ST', 'SC/ST'), ('Others', 'Others')], max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('remaining_seats_for_batch', models.PositiveIntegerField(blank=True, null=True)),
                ('display_admission_form_id_card_fees_recipt', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10)),
                ('course_fees', models.FloatField(blank=True, max_length=100, null=True)),
                ('admission_date', models.DateField(default=django.utils.timezone.now)),
                ('discount_rate', models.CharField(blank=True, choices=[('amount-', 'Amount -'), ('percent-', 'Percent -')], default='amount-', max_length=10)),
                ('discount_amount', models.FloatField(blank=True, null=True)),
                ('total_fees', models.FloatField(blank=True, default=0.0, editable=False, null=True)),
                ('fees_received', models.FloatField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('remarks', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admitted', models.BooleanField(default=False)),
                ('deletion_requested', models.BooleanField(default=False)),
                ('deletion_date', models.DateTimeField(blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.batch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('course_subject', models.JSONField(blank=True, default=list, null=True)),
                ('course_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('course_mrp', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('minimum_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('course_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('course_video_link_1', models.URLField(blank=True, null=True)),
                ('course_video_link_2', models.URLField(blank=True, null=True)),
                ('course_syllabus', models.TextField(blank=True, null=True)),
                ('eligibility', models.TextField(blank=True, null=True)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
                ('pdf_files', models.FileField(blank=True, null=True, upload_to='course_materials/')),
                ('course_video_links', models.JSONField(blank=True, default=list, null=True)),
                ('display_course_fees_on_website', models.BooleanField(blank=True, default=False, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10, null=True)),
                ('award', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.awardcategory')),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.batch')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='course_of_interest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.course'),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, default='exam', max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.DurationField(help_text='Enter the duration in HH:MM:SS format')),
                ('total_marks', models.PositiveIntegerField()),
                ('total_questions', models.PositiveIntegerField(blank=True, help_text='Enter the total number of questions', null=True)),
                ('passing_marks', models.PositiveIntegerField(blank=True, help_text='Enter the minimum passing marks', null=True)),
                ('subjects', models.JSONField(blank=True, default=list)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('appeared', 'Appeared'), ('postponed', 'Postponed'), ('cancel', 'Cancel')], max_length=10)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.batch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='users.course')),
            ],
            options={
                'verbose_name': 'Exam Status',
                'verbose_name_plural': 'Exam Statuses',
            },
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_theory_marks', models.IntegerField(blank=True, default=0, null=True)),
                ('obtained_practical_marks', models.IntegerField(blank=True, default=0, null=True)),
                ('total_mark', models.FloatField(default=0)),
                ('obtained_mark', models.FloatField(blank=True, default=0, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('grade', models.CharField(blank=True, choices=[('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=2)),
                ('result', models.CharField(blank=True, choices=[('passed', 'Passed'), ('failed', 'Failed')], max_length=7)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('subjects_data', models.JSONField(default=list)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to='users.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('certificate_no', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.batch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.course')),
                ('exam_result', models.OneToOneField(blank=True, help_text='Link to the related exam result', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_certificate', to='users.examresult')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('expiry_date', models.DateField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.course')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_mode', models.CharField(blank=True, choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('demand draft', 'Demand Draft'), ('online transfer', 'Online Transfer'), ('account adjustment', 'Account Adjustment')], max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('exam_data', models.JSONField(blank=True, default=dict, null=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.batch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('mobile', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Enter a valid mobile number.')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='support_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
