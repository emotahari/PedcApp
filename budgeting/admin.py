from django.contrib import admin

# Register your models here.
from accounts.models import Company
from budgeting.models import CostType, Currency, PublicCostType

admin.site.register(CostType)
admin.site.register(PublicCostType)