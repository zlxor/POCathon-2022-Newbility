from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

class DateInput(forms.DateInput):
    input_type = 'date'

class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Date = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    Documents = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    Hashkey = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),  required=False)
#    is_admin = forms.IntegerField(required=False)
#    is_company = forms.IntegerField(required=False)
#    is_user = forms.IntegerField(required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'Date', 'username', 'password1', 'password2', 'Documents', 'is_admin', 'is_company', 'is_user', 'Hashkey')
