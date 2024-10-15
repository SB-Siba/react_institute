from decimal import Decimal
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from PIL import Image
from django.forms import ValidationError
from django.urls import reverse
from course.models import Course
from users.manager import MyAccountManager
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from helpers import utils
import uuid
from django.conf import settings
from helpers.methods import request_deletion, cancel_deletion
from datetime import date
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid


STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
]
def generate_unique_username():
    while True:
        # Generate a random string of 8 characters (letters and digits)
        username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if the username already exists
        if not User.objects.filter(username=username).exists():
            return username
        
class Batch(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    timing = models.CharField(max_length=50, blank=True, null=True)
    number_of_students = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    YESNO = (
        ("yes", "yes"),
        ("no", "no"),
    )
    DISCOUNT_CHOICES = [
        ('amount-', 'Amount -'),
        ('percent-', 'Percent -'),
    ]

    student_image = models.ImageField(upload_to='student_photos/', max_length=250, blank=True, null=True)
    student_signature = models.ImageField(upload_to='student_signatures/', max_length=250, blank=True, null=True)
    roll_number = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=10, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.')], blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    select_one = models.CharField(max_length=10, choices=[('S/O', 'S/O'), ('D/O', 'D/O'), ('W/O', 'W/O')], blank=True)
    father_husband_name = models.CharField(max_length=100, blank=True)
    show_father_husband_on_certificate = models.BooleanField(default=False)
    surname = models.CharField(max_length=100, blank=True)
    show_surname_on_certificate = models.BooleanField(default=False)
    mother_name = models.CharField(max_length=100, blank=True)
    course_of_interest = models.ForeignKey('course.Course', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=8, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True, unique=True)
    alternative_contact = models.CharField(max_length=10, null=True, blank=True, unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, blank=True)
    city = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    permanent_address = models.TextField(blank=True)
    exam_type = models.CharField(max_length=100, choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE')], blank=True)
    referral_name = models.CharField(max_length=50, blank=True)
    referral_code = models.CharField(max_length=50, blank=True)
    aadhar_card_number = models.CharField(max_length=12, blank=True)
    caste = models.CharField(max_length=50, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    batch = models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True, blank=True)
    remaining_seats_for_batch = models.PositiveIntegerField(blank=True, null=True)
    display_admission_form_id_card_fees_recipt = models.CharField(max_length=10, choices=YESNO, default="yes")
    status = models.CharField(max_length=10, default='active')
    course_fees = models.FloatField(max_length=100, blank=True, null=True)
    admission_date = models.DateField(default=timezone.now)
    discount_rate = models.CharField(max_length=10, choices=DISCOUNT_CHOICES, default='amount-', blank=True)
    discount_amount = models.FloatField(default=0.0, null=True, blank=True)
    total_fees = models.FloatField(default=0.0, null=True, blank=True, editable=False)
    fees_received = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True, editable=False)
    remarks = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    deletion_requested = models.BooleanField(default=False)
    deletion_date = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = MyAccountManager()

    def clean(self):
        """
        Calculate the discount amount and total fees based on the discount rate and type.
        """
        if self.course_fees is None:
            raise ValidationError('Course fees must be set.')

        # Convert float values to Decimal for arithmetic operations
        course_fees = Decimal(self.course_fees) if self.course_fees else Decimal(0)
        fees_received = Decimal(self.fees_received) if self.fees_received else Decimal(0)
        
        discount_amount = Decimal(0)

        if self.discount_rate == 'amount-':
            discount_amount = min(course_fees, Decimal(self.discount_amount))
        elif self.discount_rate == 'percent-':
            discount_amount = (course_fees * Decimal(self.discount_amount)) / Decimal(100)

        self.discount_amount = discount_amount
        self.total_fees = course_fees - discount_amount
        self.balance = self.total_fees - fees_received

        # Ensure balance is non-negative
        if self.balance < 0:
            raise ValidationError('Balance cannot be negative.')

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Generates an 8-character string like "G4U6PB5T"
        
        if not self.password:
            self.password = ''.join(random.choices(string.digits, k=10))  # Generates a 10-digit string like "9364528710"


        if self.course_of_interest:
            self.course_fees = self.course_of_interest.course_fees
        else:
            self.course_fees = 0.0
        self.clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class Installment(models.Model):
    student = models.ForeignKey(User, related_name='installments', on_delete=models.CASCADE)
    installment_name = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.installment_name} - {self.amount}"
        
class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Franchise(models.Model):
    approved = models.BooleanField(default=False)
    action = models.TextField()
    logo = models.ImageField(upload_to='franchise_logos/')
    institute_name = models.CharField(max_length=255)
    no_of_students = models.IntegerField(default=0)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    atc_code = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.institute_name
    
class ReferralSettings(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=300.00)

    def __str__(self):
        return f"Referral Amount: {self.amount}"

class OnlineClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    expiry_date = models.DateField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    
