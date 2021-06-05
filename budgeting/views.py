from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from budgeting.forms import IncomeAdd
from budgeting.models import Income


def income_view(request):
    if request.method == 'POST':
        fm = IncomeAdd(request.POST)
        if fm.is_valid():
            fm.save()
            fm = IncomeAdd()
    else:
        fm = IncomeAdd()
        incomeList = Income.objects.all()
    return render(request, 'budgeting/incomecrud.html', {'form': fm, 'incomeList': incomeList})
