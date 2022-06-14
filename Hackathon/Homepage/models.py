from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    first_name = models.CharField(max_length=200, help_text='Enter first name')
    last_name = models.CharField(max_length=200, help_text='Enter last name')
    DOB = models.CharField(max_length=200, help_text='Enter date of birth')
    emailaddress = models.CharField(max_length=200, help_text='Enter email address')
    password = models.CharField(max_length=200, help_text='Enter password)')
    documents = models.CharField(max_length=200, help_text='Uploaded documents')

    def get_absolute_url(self):
        return reverse('User-detail', args=[str(self.id)])

    def __str__(self):
        return self.emailaddress