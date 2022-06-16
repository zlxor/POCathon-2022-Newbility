from django.contrib import admin
from .models import CompanyProfile, UserProfile

admin.site.register(UserProfile)
admin.site.register(CompanyProfile)