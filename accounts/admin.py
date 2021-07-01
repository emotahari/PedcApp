from django.contrib import admin

# Register your models here.
from accounts.models import Company, ProfileAuth
from budgeting.models import Currency

admin.site.register(Company)
admin.site.register(Currency)
admin.site.register(ProfileAuth)
