from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from apps.accounts.models import User


class RegistrationStep1Form(forms.Form):
    """Personal information — Step 1 of registration."""

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '024 000 0000'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )
    terms = forms.BooleanField(
        label='I agree to the Terms and Conditions',
        error_messages={'required': 'You must accept the terms and conditions to register.'}
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number'].strip()
        # Normalize Ghana numbers
        phone = phone.replace(' ', '').replace('-', '')
        if phone.startswith('0') and len(phone) == 10:
            return phone
        if phone.startswith('+233') and len(phone) == 13:
            return phone
        if phone.startswith('233') and len(phone) == 12:
            return phone
        raise forms.ValidationError('Enter a valid Ghana phone number (e.g. 024 000 0000).')

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                raise forms.ValidationError(e.messages)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError({'password2': 'Passwords do not match.'})
        return cleaned_data


class RegistrationStep2Form(forms.Form):
    """School information — Step 2 of registration."""

    school_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Future People Academy'})
    )
    school_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'school@email.com'})
    )
    school_phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '030 000 0000'})
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Accra'})
    )
    country = forms.CharField(
        max_length=100,
        initial='Ghana',
        widget=forms.TextInput(attrs={'placeholder': 'Ghana'})
    )
    logo = forms.ImageField(
        required=False,
        widget=forms.FileInput()
    )

    def clean_school_email(self):
        from apps.tenants.models import School
        email = self.cleaned_data['school_email'].lower()
        if School.objects.filter(email=email).exists():
            raise forms.ValidationError('A school with this email is already registered.')
        return email


class OTPVerificationForm(forms.Form):
    """SMS OTP verification form."""

    otp = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'placeholder': '000000',
            'maxlength': '6',
            'autocomplete': 'one-time-code',
            'inputmode': 'numeric',
        })
    )

    def clean_otp(self):
        otp = self.cleaned_data['otp'].strip()
        if not otp.isdigit():
            raise forms.ValidationError('Enter the 6-digit code sent to your phone.')
        return otp