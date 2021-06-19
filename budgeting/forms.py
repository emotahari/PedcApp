from django import forms

from budgeting.models import Income, CostOfSales


class IncomeAdd(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


class CostAddShow(forms.ModelForm):
    class Meta:
        model = CostOfSales
        fields = '__all__'
