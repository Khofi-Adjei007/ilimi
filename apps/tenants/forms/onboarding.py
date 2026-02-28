from django import forms


class BranchSetupForm(forms.Form):
    """First branch setup during onboarding."""

    branch_name = forms.CharField(
        max_length=255,
        initial='Main Campus',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Main Campus'})
    )
    branch_code = forms.CharField(
        max_length=20,
        initial='MAIN',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. MAIN'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Full address of this branch',
            'rows': 3
        })
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Accra'})
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Branch phone number'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Branch email (optional)'})
    )