from django import forms

CHOICES = [ ('Company','Company'), ('Individual','Individual'),]

class LoginForm(forms.Form):
    Choice = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-select"}, choices=CHOICES), required=True)
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

#class DateInput(forms.DateInput):
#    input_type = 'date'
#
#class SignupForm(forms.Form):
#    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
#    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
#    Date = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
#    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
#    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
#    Documents = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

