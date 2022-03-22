from django.contrib import admin

# Register your models here.
from accounts.models import Company
from budgeting.models import CostType, Currency, PublicCostType, CurrentAssetsType, NonCurrentAssetsType, \
    CurrentLiabilitiesType, NonCurrentLiabilitiesType, PropertyRightsType, Csv, FinanceMegaData

admin.site.register(CostType)
admin.site.register(PublicCostType)
admin.site.register(CurrentAssetsType)
admin.site.register(NonCurrentAssetsType)
admin.site.register(CurrentLiabilitiesType)
admin.site.register(NonCurrentLiabilitiesType)
admin.site.register(PropertyRightsType)
admin.site.register(Csv)
admin.site.register(FinanceMegaData)
