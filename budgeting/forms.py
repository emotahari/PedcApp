from django import forms

from budgeting.models import Income, CostOfSales, PublicCost, EtcOprationalIncome, EtcOprationalCost, NonOprationalCost, \
    NonOprationalIncome, Tax, LoanCost


class IncomeAddForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


class CostAddShow(forms.ModelForm):
    class Meta:
        model = CostOfSales
        fields = '__all__'


class PublicCostForm(forms.ModelForm):
    class Meta:
        model = PublicCost
        fields = '__all__'


class EtcOprationlIncomeForm(forms.ModelForm):
    class Meta:
        model = EtcOprationalIncome
        fields = '__all__'


class EtcOprationlCostForm(forms.ModelForm):
    class Meta:
        model = EtcOprationalCost
        fields = '__all__'


class NonOprationlIncometForm(forms.ModelForm):
    class Meta:
        model = NonOprationalIncome
        fields = '__all__'


class NonOprationlCostForm(forms.ModelForm):
    class Meta:
        model = NonOprationalCost
        fields = '__all__'


class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = '__all__'


class LoanCostForm(forms.ModelForm):
    class Meta:
        model = LoanCost
        fields = '__all__'
