from django import forms
from .models import UserProfile, CompanyProfile

class DateInput(forms.DateInput):
    input_type = 'date'

class UserSignup(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    DOB = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    emailaddress = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    documents = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = UserProfile
        exclude = ("Hashkey", )

class CompanySignup(forms.ModelForm):
    Companyname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    UEN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    DOI = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    emailaddress = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    documents = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = CompanyProfile
        exclude = ("Hashkey", )