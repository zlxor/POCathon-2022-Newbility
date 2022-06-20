from django.contrib import admin
from .models import JobListing, Company, Individual

admin.site.register(JobListing)
admin.site.register(Company)
admin.site.register(Individual)

