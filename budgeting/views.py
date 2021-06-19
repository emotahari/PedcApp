from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from accounts.models import Company
from budgeting.forms import IncomeAdd, CostAddShow
from budgeting.models import Income, Currency, CostType


#  incomAdd
def income_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    currency = Currency.objects.all()
    context = {
        'companys': company

    }
    newIncome = Income()
    newCurrency = Currency()
    newCompany = Company()
    newCurrency.id = request.POST.get('currency', 1)
    newCompany.id = request.POST.get('currency', 1)
    newIncome.forcastIncomeQ1 = request.POST.get('forcastIncomeQ1', 0)
    newIncome.forcastIncomeQ2 = request.POST.get('forcastIncomeQ2', 0)
    newIncome.forcastIncomeQ3 = request.POST.get('forcastIncomeQ3', 0)
    newIncome.forcastIncomeQ4 = request.POST.get('forcastIncomeQ4', 0)
    newIncome.realIncomeQ1 = request.POST.get('realIncomeQ1', 0)
    newIncome.realIncomeQ2 = request.POST.get('realIncomeQ2', 0)
    newIncome.realIncomeQ3 = request.POST.get('realIncomeQ3', 0)
    newIncome.realIncomeQ4 = request.POST.get('realIncomeQ4', 0)
    newIncome.projectName = request.POST.get('projectName', 0)
    newIncome.yearOfForcast = request.POST.get('yearOfForcast', 1400)
    newIncome.isInGroupe = request.POST.get('isInGroupe', 0)
    # newIncome.currency = newCurrency.id
    # newIncome.company = newCompany.id
    if request.method == 'POST':
        Income.objects.create(
            projectName=newIncome.projectName,
            realIncomeQ1=newIncome.realIncomeQ1,
            realIncomeQ2=newIncome.realIncomeQ2,
            realIncomeQ3=newIncome.realIncomeQ3,
            realIncomeQ4=newIncome.realIncomeQ4,
            forcastIncomeQ1=newIncome.forcastIncomeQ1,
            forcastIncomeQ2=newIncome.forcastIncomeQ2,
            forcastIncomeQ3=newIncome.forcastIncomeQ3,
            forcastIncomeQ4=newIncome.forcastIncomeQ4,
            yearOfForcast=newIncome.yearOfForcast,
            isInGroupe=newIncome.isInGroupe,
            currency=newCurrency,
            company=newCompany,
        )
        incomelist = Income.objects.filter(company=company_id)
    else:
        incomelist = Income.objects.filter(company=company_id)

        # newIncome.save()
    return render(request, 'budgeting/incomecrud00.html',
                  {'companies': company, 'currencies': currency, 'incomeList': incomelist})

    #  income delete


def delete_income_data(request, id):
    if request.method == 'POST':
        deleted_income = Income.objects.get(pk=id)
        companyid = deleted_income.company.id
        deleted_income.delete()
    return redirect('budgeting:income', companyid)
    # return redirect(income_view(request, company_id=Income.company.id))

    # income edit


def update_income_data(request, incomeId):
    if request.method == 'POST':
        ui = Income.objects.get(pk=incomeId)
        form = IncomeAdd(request.POST, instance=ui)
        if form.is_valid():
            form.save()
        else:
            ui = Income.objects.get(pk=incomeId)
            form = IncomeAdd(instance=ui)
    else:
        ui = Income.objects.get(pk=incomeId)
        form = IncomeAdd(instance=ui)
    return render(request, 'budgeting/incomeupdate.html', {'form': form})


# ########################  CostOfSales  ################################

# ######## Add Viwe  ####################################################

def addCostOfSales(request, id):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    costType = CostType.objects.all()
    fg = CostAddShow()
    return render(request, 'budgeting/costofsales.html', {'form': fg, 'companies': company, 'currency': currency
                                                          ,'costType': costType})
