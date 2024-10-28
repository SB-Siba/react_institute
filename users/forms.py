import re
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from users.models import Batch, OnlineClass, User, Installment, Payment, User, Course
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django import forms
from django.forms.widgets import HiddenInput

class SignUpForm(forms.Form):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Full Name'}))
    email = forms.EmailField(max_length=254,
    widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Valid Email Address'}))
    contact = forms.CharField(max_length=10,
    validators=[RegexValidator(regex='^[9876]\d{9}$')],widget=forms.TextInput(attrs={'class': 'form-control','Placeholder':'Enter Mobile Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Confirm Password'}))



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists")
        return email

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if User.objects.filter(contact=contact).exists():
            raise forms.ValidationError("Contact number already exists")
        return contact


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6 :
            raise ValidationError('Password length must be 6 characters.')

        if not re.search(r'[A-Za-z]', password):
            raise ValidationError('Password must contain at least one alphabet.')

        if not re.search(r'[0-9]', password):
            raise ValidationError('Password must contain at least one number.')

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('Password must contain at least one special character.')

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Valid Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Password'}))
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user found with this email address.")
        return email
 
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
 


class UpdateProfileForm(forms.Form):
    
    email = forms.EmailField(max_length=255)
    email.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Email',"required":"required"})

    full_name = forms.CharField(max_length=255)
    full_name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Full Name',"required":"required"})

    contact = forms.CharField(max_length=10,help_text='Required. Enter Mobile Number',
    validators=[RegexValidator(regex='^[9876]\d{9}$')],widget=forms.TextInput(attrs={'class': 'form-control'}))

    profile_pic = forms.FileField(label='Select an image file', required=False)
    profile_pic.widget.attrs.update({'class': 'form-control', 'type': 'file'})




class AddressForm(forms.Form):
    Address1 = forms.CharField(max_length=255)
    Address1.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    Address2 = forms.CharField(max_length=255)
    Address2.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    contact = forms.CharField(max_length=10,help_text='Required. Enter Mobile Number',
    validators=[RegexValidator(regex='^[9876]\d{9}$')],widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    country = forms.CharField(max_length=255)
    country.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    state = forms.CharField(max_length=255)
    state.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    city = forms.CharField(max_length=255)
    city.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})
    
    pincode = forms.IntegerField()
    pincode.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Pincode',"required":"required"})



class EditUserForm(forms.Form):
    model =User
    email = forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    full_name = forms.CharField(label="Full Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    contact = forms.IntegerField(label="Contact",widget=forms.NumberInput(attrs={"class":"form-control"}))



class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'contact', 'password']  # Include necessary fields

    # Optionally, you can add custom validation or widgets
    password = forms.CharField(widget=forms.PasswordInput)

class StudentForm(forms.ModelForm):
    total_fees = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    balance = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = [
            'student_image', 'student_signature', 'roll_number', 'abbreviation',
            'full_name', 'select_one', 'father_husband_name', 'show_father_husband_on_certificate',
            'surname', 'show_surname_on_certificate', 'mother_name', 'course_of_interest',
            'email', 'contact', 'alternative_contact', 'date_of_birth',
            'gender', 'state', 'city', 'pincode', 'permanent_address', 'exam_type',
            'referral_code', 'aadhar_card_number', 'caste', 'qualification', 'occupation',
            'course_fees', 'discount_rate', 'discount_amount',
            'fees_received',
            'remarks', 'batch', 'remaining_seats_for_batch',
            'display_admission_form_id_card_fees_recipt'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
            'display_admission_form_id_card_fees_recipt': forms.RadioSelect(choices=User.YESNO),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError("Please enter a valid email address.")
        return email

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not re.match(r"^[6-9]\d{9}$", contact):  # Only 10-digit numbers starting with 6-9
            raise ValidationError("Please enter a valid 10-digit phone number.")
        return contact

    def clean_aadhar_card_number(self):
        aadhar = self.cleaned_data.get('aadhar_card_number')
        if not re.match(r"^\d{12}$", aadhar):  # Exactly 12 digits
            raise ValidationError("Please enter a valid 12-digit Aadhaar number.")
        return aadhar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['father_husband_name'].label = "Father/husband name"
        self.fields['show_father_husband_on_certificate'].label = "Show father/husband on certificate"

        if self.instance and self.instance.pk:
            self.fields['total_fees'].initial = self.instance.total_fees
            self.fields['balance'].initial = self.instance.balance
        
        self.fields['roll_number'].widget.attrs.update({
            'placeholder': 'ROLL0001'
        })
        self.fields['full_name'].widget.attrs.update({
            'placeholder': 'Enter full name'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter email address'
        })
        self.fields['contact'].widget.attrs.update({
            'placeholder': 'Enter contact number'
        })
        

class ReAdmissionForm(forms.Form):
    student = forms.ModelChoiceField(queryset=User.objects.filter(course_of_interest__isnull=False), required=True, label="Select Student")
    course_of_interest = forms.ModelChoiceField(queryset=Course.objects.filter(status='Active'), required=True, label="Course of Interest")
    exam_type = forms.ChoiceField(choices=[('OFFLINE', 'OFFLINE'), ('ONLINE', 'ONLINE')], required=True, label="Select Exam Type")
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=True)
    # Hidden fields for fees, discount, and other details that will be updated dynamically
    course_fees = forms.DecimalField(required=False, widget=forms.HiddenInput())
    discount_rate = forms.CharField(required=False, widget=forms.HiddenInput())
    discount_amount = forms.DecimalField(required=False, widget=forms.HiddenInput())
    total_fees = forms.DecimalField(required=False, widget=forms.HiddenInput())
    fees_received = forms.DecimalField(required=False, widget=forms.HiddenInput())
    balance = forms.DecimalField(required=False, widget=forms.HiddenInput())

class InstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = ['installment_name', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise forms.ValidationError("Amount must be a positive number.")
        return amount

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise forms.ValidationError("Date is required.")
        return date

class StudentPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'course', 'amount', 'payment_mode', 'description']  # Define the fields to be used
        widgets = {
            'amount': forms.NumberInput(attrs={'value': '0.00', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    # Additional fields for balance amount and payment mode choices
    balance = forms.DecimalField(label='Total Balance Amount', max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    payment_mode = forms.ChoiceField(
        choices=[
            ('', '--select--'),
            ('cash', 'Cash'),
            ('cheque', 'Cheque'),
            ('demand draft', 'Demand Draft'),
            ('online transfer', 'Online Transfer'),
            ('account adjustment', 'Account Adjustment')
        ],
        label='Payment Mode',
    )

    # Override the __init__ method to populate the dropdowns dynamically
    def __init__(self, *args, **kwargs):
        super(StudentPaymentForm, self).__init__(*args, **kwargs)
        # Dynamically populate the student dropdown with users who are students
        self.fields['student'].queryset = User.objects.filter(is_superuser=False)  # Assuming `is_superuser=False` indicates students
        # Dynamically populate the course dropdown with available courses
        self.fields['course'].queryset = Course.objects.all()

class OnlineClassForm(forms.ModelForm):
    class Meta:
        model = OnlineClass
        fields = ['course', 'title', 'link', 'description', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['name', 'timing','number_of_students','total_seats']