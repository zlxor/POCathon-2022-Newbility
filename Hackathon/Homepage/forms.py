from django import forms

from Homepage.models import JobListing, Individual, Company


class LoginForm(forms.Form):
    USERORCOMPANY = [ ('1','Company'), ('2','Individual'),]
    Choice = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), choices=USERORCOMPANY)
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

class UserSignupForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),required=True)
    Phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),required=True)
    Resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Individual
        fields = '__all__'

class CompanySignupForm(forms.ModelForm):
    CompanyName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    UEN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Industry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    Documents = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Company
        fields = '__all__'

class PostJobs(forms.ModelForm):
    Locations = [ ('1','Pasir Ris'), ('2','Raffles'), ('3','City Hall'), ('4','Tampines'), ('5','Bugis'), ('6','Jurong East'),
                  ('7','Outram Park'), ('8','Hougang'), ('9','Woodlands'), ('10','Bukit Batok'), ('11','Yew Tee'), ('12','Pioneer'),]
    Department = forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control border-0", 'placeholder':"Department", 'style':"height: 55px;"}),required=True)
    Location = forms.ChoiceField(widget=forms.Select(attrs={'class' : "form-select border-0", 'style' : "height: 55px;"}), choices = Locations)
    JobTitle = forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control border-0", 'placeholder':"Job Title", 'style':"height: 55px;"}),required=True)
    Salary = forms.IntegerField(widget=forms.TextInput(attrs={'class' : "form-control border-0", 'placeholder':"Salary", 'style':"height: 55px;"}),required=True)
    JobDescription = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control border-0", 'rows':"5", 'placeholder':"Job Description"}),required=True)

    class Meta:
        model = JobListing
        fields = '__all__'

