
from django import forms

from budgeting.models import Income


class IncomeAdd(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['projectName', 'realIncomeQ1', 'realIncomeQ2', 'realIncomeQ3','realIncomeQ4',
                  'forcastIncomeQ1','forcastIncomeQ2','forcastIncomeQ3','forcastIncomeQ4',
                  'yearOfForcast', 'isInGroupe', 'currency']
        widgets = {
            'projectName': forms.TextInput(attrs={'class': 'form-control'}),
            'realIncomeQ1': forms.TextInput(attrs={'class': 'form-control'}),
            'realIncomeQ2': forms.TextInput(attrs={'class': 'form-control'}),
            'realIncomeQ3': forms.TextInput(attrs={'class': 'form-control'}),
            'realIncomeQ4': forms.TextInput(attrs={'class': 'form-control'}),
            'forcastIncomeQ1': forms.TextInput(attrs={'class': 'form-control'}),
            'forcastIncomeQ2': forms.TextInput(attrs={'class': 'form-control'}),
            'forcastIncomeQ3': forms.TextInput(attrs={'class': 'form-control'}),
            'forcastIncomeQ4': forms.TextInput(attrs={'class': 'form-control'}),
            'yearOfForcast': forms.TextInput(attrs={'class': 'form-control'}),
            'isInGroupe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'company': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }
