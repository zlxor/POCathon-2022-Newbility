from django.db import models



class Individual(models.Model):
    Email = models.EmailField(max_length=200)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Resume = models.FileField(max_length=200)

    def __str__(self):
        return self.Email

class Company(models.Model):
    CompanyName = models.CharField(max_length=200)
    UEN = models.CharField(max_length=200)
    Industry = models.CharField(max_length=200)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=200)
    Documents = models.FileField(max_length=200)

    def __str__(self):
        return self.CompanyName

class JobListing(models.Model):
    Company = models.ManyToManyField(Company)
    Department = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    JobTitle = models.CharField(max_length=200)
    Salary = models.IntegerField()
    JobDescription = models.CharField(max_length=200)

    def __str__(self):
        return self.Company, self.JobTitle
