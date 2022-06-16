from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    first_name = models.CharField(max_length=200, help_text='Enter first name')
    last_name = models.CharField(max_length=200, help_text='Enter last name')
    DOB = models.DateField(help_text='Enter date of birth')
    emailaddress = models.EmailField(max_length=200, help_text='Enter email address')
    password = models.CharField(max_length=200, help_text='Enter password)')
    documents = models.CharField(max_length=200, help_text='Uploaded documents')
    Hashkey = models.CharField(max_length=200, help_text='ModelHash',default="")

    def get_absolute_url(self):
        return reverse('User-detail', args=[str(self.id)])

    def __str__(self):
        return self.emailaddress

class CompanyProfile(models.Model):
    Companyname = models.CharField(max_length=200, help_text='Enter company name')
    UEN = models.CharField(max_length=200, help_text='Enter UEN')
    DOI = models.DateField(help_text='Enter date of incorporation')
    emailaddress = models.EmailField(max_length=200, help_text='Enter email address')
    password = models.CharField(max_length=200, help_text='Enter password)')
    documents = models.CharField(max_length=200, help_text='Uploaded documents')
    Hashkey = models.CharField(max_length=200, help_text='ModelHash',default="")

    def get_absolute_url(self):
        return reverse('Company-detail', args=[str(self.id)])

    def __str__(self):
        return self.emailaddress