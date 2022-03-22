from django import forms

from budgeting.models import Income, CostOfSales, PublicCost, EtcOprationalIncome, EtcOprationalCost, NonOprationalCost, \
    NonOprationalIncome, Tax, LoanCost, CurrentAsset, NonCurrentAsset, CurrentLiabilitiesType, \
    NonCurrentLiabilitiesType, PropertyRights, CurrentLiabilities, NonCurrentLiabilities, Csv
from lib.validators import positive_check


class IncomeAddForm(forms.ModelForm):
    realIncomeQ1 = forms.IntegerField(validators=[positive_check])
    realIncomeQ2 = forms.IntegerField(validators=[positive_check])
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

class CrrntAsstForm(forms.ModelForm):
    class Meta:
        model = CurrentAsset
        fields = '__all__'

class NCrrntAsstForm(forms.ModelForm):
    class Meta:
        model = NonCurrentAsset
        fields = '__all__'


class CrrntLbltForm(forms.ModelForm):
    class Meta:
        model = CurrentLiabilities
        fields = '__all__'

class NCrrntLbltForm(forms.ModelForm):
    class Meta:
        model = NonCurrentLiabilities
        fields = '__all__'

class PrprtyRightsForm(forms.ModelForm):
    class Meta:
        model = PropertyRights
        fields = '__all__'

class UploadCsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = '__all__'

