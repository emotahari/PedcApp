from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from accounts.models import Company
from budgeting.forms import IncomeAdd
from budgeting.models import Income


def income_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    # company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        fm = IncomeAdd(request.POST)
        if fm.is_valid():
            fm.save()
            fm = IncomeAdd()
    else:
        fm = IncomeAdd()
        incomelist = Income.objects.all()
    return render(request, 'budgeting/incomecrud.html', {'form': fm, 'icList': incomelist, 'company': company})
