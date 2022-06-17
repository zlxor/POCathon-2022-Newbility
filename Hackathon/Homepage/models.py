from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    is_company = models.BooleanField('Company',default = False)
    is_user = models.BooleanField('User',default = False)
    is_admin = models.BooleanField('Admin',default = False)
    Date = models.DateField(help_text='Date of Birth/Incorporation',  default = "1900-01-01")
    Documents = models.CharField(max_length = 1000, help_text='Uploaded documents',  default = "")
    Hashkey = models.CharField(max_length = 1000, help_text='Affindi-Hash',  default = "")
#
#    def get_absolute_url(self):
#        return reverse('User-detail', args=[str(self.id)])
#
#    def __str__(self):
#        return self.emailaddress
#
#class CompanyProfile(models.Model):
#    Companyname = models.CharField(max_length=200, help_text='Enter company name')
#    UEN = models.CharField(max_length=200, help_text='Enter UEN')
#    DOI = models.DateField(help_text='Enter date of incorporation')
#    emailaddress = models.EmailField(max_length=200, help_text='Enter email address')
#    password = models.CharField(max_length=200, help_text='Enter password)')
#    documents = models.CharField(max_length=200, help_text='Uploaded documents')
#    Hashkey = models.CharField(max_length=200, help_text='ModelHash',default="")
#
#    def get_absolute_url(self):
#        return reverse('Company-detail', args=[str(self.id)])
#
#    def __str__(self):
#        return self.emailaddress