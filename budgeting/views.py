from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from accounts.models import Company, ProfileAuth
from budgeting.forms import  CostAddShow, PublicCostForm, EtcOprationlIncomeForm, EtcOprationlCostForm, \
    NonOprationlIncometForm, NonOprationlCostForm, TaxForm, LoanCostForm, IncomeAddForm
from budgeting.models import Income, Currency, CostType, CostOfSales, PublicCostType, PublicCost, EtcOprationalIncome, \
    EtcOprationalCost, NonOprationalIncome, NonOprationalCost, Tax, LoanCost


#  incomAdd
@login_required
def income_view(request, company_id, incomeid=0):
    company = get_object_or_404(Company, pk=company_id)
    currency = Currency.objects.all()
    # income = CostType.objects.all()
    incomeList = Income.objects.filter(company=company_id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if company_id in b:
        if request.method == "GET":
            if incomeid == 0:
                form = IncomeAddForm()
            else:
                incomeList1 = Income.objects.get(pk=incomeid)
                form = IncomeAddForm(instance=incomeList1)
            return render(request, 'budgeting/incomecrud00.html',
                          {'form': form, 'companies': company, 'currency': currency
                              , 'incomeList': incomeList, 'userAuth': b})
        else:
            if incomeid == 0:
                form = IncomeAddForm(request.POST)
            else:
                incomeList1 = Income.objects.get(pk=incomeid)
                form = IncomeAddForm(request.POST, instance=incomeList1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/incomecrud00.html',
                          {'form': form, 'companies': company, 'currency': currency
                              , 'incomeList': incomeList, 'userAuth': b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))


    # ---------------------------------------
    # company = get_object_or_404(Company, pk=company_id)
    # currency = Currency.objects.all()
    # context = {
    #     'companys': company
    #
    # }
    # newIncome = Income()
    # newCurrency = Currency()
    # newCompany = Company()
    # newCurrency.id = request.POST.get('currency', 1)
    # newCompany.id = request.POST.get('company', 1)
    # newIncome.forcastIncomeQ1 = request.POST.get('forcastIncomeQ1', 0)
    # newIncome.forcastIncomeQ2 = request.POST.get('forcastIncomeQ2', 0)
    # newIncome.forcastIncomeQ3 = request.POST.get('forcastIncomeQ3', 0)
    # newIncome.forcastIncomeQ4 = request.POST.get('forcastIncomeQ4', 0)
    # newIncome.realIncomeQ1 = request.POST.get('realIncomeQ1', 0)
    # newIncome.realIncomeQ2 = request.POST.get('realIncomeQ2', 0)
    # newIncome.realIncomeQ3 = request.POST.get('realIncomeQ3', 0)
    # newIncome.realIncomeQ4 = request.POST.get('realIncomeQ4', 0)
    # newIncome.projectName = request.POST.get('projectName', 0)
    # newIncome.yearOfForcast = request.POST.get('yearOfForcast', 1400)
    # newIncome.isInGroupe = request.POST.get('isInGroupe', 0)
    # newIncome.currency = newCurrency.id
    # newIncome.company = newCompany.id
    # if request.method == 'POST':
    #     Income.objects.create(
    #         projectName=newIncome.projectName,
    #         realIncomeQ1=newIncome.realIncomeQ1,
    #         realIncomeQ2=newIncome.realIncomeQ2,
    #         realIncomeQ3=newIncome.realIncomeQ3,
    #         realIncomeQ4=newIncome.realIncomeQ4,
    #         forcastIncomeQ1=newIncome.forcastIncomeQ1,
    #         forcastIncomeQ2=newIncome.forcastIncomeQ2,
    #         forcastIncomeQ3=newIncome.forcastIncomeQ3,
    #         forcastIncomeQ4=newIncome.forcastIncomeQ4,
    #         yearOfForcast=newIncome.yearOfForcast,
    #         isInGroupe=newIncome.isInGroupe,
    #         currency=newCurrency,
    #         company=newCompany,
    #     )
    #     incomelist = Income.objects.filter(company=company_id)
    # else:
    #     incomelist = Income.objects.filter(company=company_id)
    #
    #     # newIncome.save()
    # return render(request, 'budgeting/incomecrud00.html',
    #               {'companies': company, 'currencies': currency, 'incomeList': incomelist})

    #  income delete

# @login_required
# def delete_income_data(request, id):
#     if request.method == 'POST':
#         deleted_income = Income.objects.get(pk=id)
#         companyid = deleted_income.company.id
#         deleted_income.delete()
#     return redirect('budgeting:income', companyid)
#

@login_required
def delete_income_data(request, id):
    # if request.method == 'POST':
    #     deleted_income = Income.objects.get(pk=id)
    #     companyid = deleted_income.company.id
    #     deleted_income.delete()
    return render(request, 'budgeting/modal.html', {'form': id})



    # income edit

@login_required
def update_income_data(request, incomeId):
    if request.method == 'POST':
        ui = Income.objects.get(pk=incomeId)
        form = IncomeAddForm(request.POST, instance=ui)
        if form.is_valid():
            form.save()
        else:
            ui = Income.objects.get(pk=incomeId)
            form = IncomeAddForm(instance=ui)
    else:
        ui = Income.objects.get(pk=incomeId)
        form = IncomeAddForm(instance=ui)
    return render(request, 'budgeting/incomeupdate.html', {'form': form})


# ########################  CostOfSales  ################################

# ######## ADD Viwe  #####  CostOfSales  ################################
@login_required
def addCostOfSales(request, id, costid=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    costType = CostType.objects.all()
    costOfSales = CostOfSales.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if costid == 0:
                form = CostAddShow()
            else:
                costOfSales1 = CostOfSales.objects.get(pk=costid)
                form = CostAddShow(instance=costOfSales1)
            return render(request, 'budgeting/costofsales.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'costType': costType, 'costOfSales': costOfSales, 'userAuth':b})
        else:
            if costid == 0 :
                form = CostAddShow(request.POST)
            else:
                costOfSales1 = CostOfSales.objects.get(pk=costid)
                form = CostAddShow(request.POST, instance=costOfSales1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/costofsales.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'costType': costType, 'costOfSales': costOfSales, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))

# ######## DELETE Viwe  #####  CostOfSales  ################################


# ########   START   ##########  PublicCost  ##########################

# ######## ADD Viwe  ##########  PublicCost  ##########################


@login_required
def addPublicCost(request, id, pubCostId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    publicCostType = PublicCostType.objects.all()
    publicCost = PublicCost.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if pubCostId == 0:
                form = PublicCostForm()
            else:
                publicCost1 = PublicCost.objects.get(pk=pubCostId)
                form = PublicCostForm(instance=publicCost1)
            return render(request, 'budgeting/publiccost.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'publicCostType': publicCostType, 'publicCost': publicCost, 'userAuth':b})
        else:
            if pubCostId == 0 :
                form = PublicCostForm(request.POST)
            else:
                publicCost1 = PublicCost.objects.get(pk=pubCostId)
                form = PublicCostForm(request.POST, instance=publicCost1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/publiccost.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'publicCostType': publicCostType, 'publicCost': publicCost, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


# ########   START   ##########  EtcOprationlIncome  ##########################

# ######## ADD Viwe  ##########  EtcOprationlIncome  ##########################


@login_required
def addEtcOprationlIncome(request, id, etcOprInId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    etcOpratinalIncome = EtcOprationalIncome.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if etcOprInId == 0:
                form = EtcOprationlIncomeForm()
            else:
                etcOpratinalIncome1 = EtcOprationalIncome.objects.get(pk=etcOprInId)
                form = EtcOprationlIncomeForm(instance=etcOpratinalIncome1)
            return render(request, 'budgeting/etcoprincome.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'etcOpratinalIncome': etcOpratinalIncome, 'userAuth':b})
        else:
            if etcOprInId == 0 :
                form = EtcOprationlIncomeForm(request.POST)
            else:
                etcOpratinalIncome1 = EtcOprationalIncome.objects.get(pk=etcOprInId)
                form = EtcOprationlIncomeForm(request.POST, instance=etcOpratinalIncome1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/etcoprincome.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'etcOpratinalIncome': etcOpratinalIncome, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


# ########   START   ##########  EtcOprationalCost  ##########################

# ######## ADD Viwe  ##########  EtcOprationalCost  ##########################


@login_required
def addEtcOprationalCost(request, id, etcOprCoctId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    etcOprCoct = EtcOprationalCost.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if etcOprCoctId == 0:
                form = EtcOprationlCostForm()
            else:
                etcOprCoct1 = EtcOprationalCost.objects.get(pk=etcOprCoctId)
                form = EtcOprationlCostForm(instance=etcOprCoct1)
            return render(request, 'budgeting/etcoprcost.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'etcOprCoct': etcOprCoct, 'userAuth':b})
        else:
            if etcOprCoctId == 0 :
                form = EtcOprationlCostForm(request.POST)
            else:
                etcOprCoct1 = EtcOprationalCost.objects.get(pk=etcOprCoctId)
                form = EtcOprationlCostForm(request.POST, instance=etcOprCoct1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/etcoprcost.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'etcOprCoct': etcOprCoct, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


# ########   START   ##########  NonOprationalIncome  ##########################

# ######## ADD Viwe  ##########  NonOprationalIncome  ##########################


@login_required
def addNonOprationalIncome(request, id, nonOprInId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    nonOpratinalIncome = NonOprationalIncome.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if nonOprInId == 0:
                form = NonOprationlIncometForm()
            else:
                nonOpratinalIncome1 = NonOprationalIncome.objects.get(pk=nonOprInId)
                form = NonOprationlIncometForm(instance=nonOpratinalIncome1)
            return render(request, 'budgeting/nonoprincome.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'nonOpratinalIncome': nonOpratinalIncome, 'userAuth':b})
        else:
            if nonOprInId == 0 :
                form = NonOprationlIncometForm(request.POST)
            else:
                nonOpratinalIncome1 = NonOprationalIncome.objects.get(pk=nonOprInId)
                form = NonOprationlIncometForm(request.POST, instance=nonOpratinalIncome1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/nonoprincome.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'nonOpratinalIncome': nonOpratinalIncome, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


# ########   START   ##########  NonOprationalCost  ##########################

# ######## ADD Viwe  ##########  NonOprationalCost  ##########################


@login_required
def addNonOprationalCost(request, id, nonOprostId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    nonOpratinalCost = NonOprationalCost.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if nonOprostId == 0:
                form = NonOprationlCostForm()
            else:
                nonOpratinalCost1 = NonOprationalCost.objects.get(pk=nonOprostId)
                form = NonOprationlCostForm(instance=nonOpratinalCost1)
            return render(request, 'budgeting/nonoprcost.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'nonOpratinalCost': nonOpratinalCost, 'userAuth':b})
        else:
            if nonOprostId == 0 :
                form = NonOprationlCostForm(request.POST)
            else:
                nonOpratinalCost1 = NonOprationalCost.objects.get(pk=nonOprostId)
                form = NonOprationlCostForm(request.POST, instance=nonOpratinalCost1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/nonoprcost.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'nonOpratinalCost': nonOpratinalCost, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


# ########   START   ##########  Tax  ##########################

# ######## ADD Viwe  ##########  Tax  ##########################


@login_required
def addTax(request, id, taxId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    tax = Tax.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if taxId == 0:
                form = TaxForm()
            else:
                tax1 = Tax.objects.get(pk=taxId)
                form = TaxForm(instance=tax1)
            return render(request, 'budgeting/tax.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'tax': tax, 'userAuth':b})
        else:
            if taxId == 0 :
                form = TaxForm(request.POST)
            else:
                tax1 = Tax.objects.get(pk=taxId)
                form = TaxForm(request.POST, instance=tax1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/tax.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'tax': tax, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


# ########   START   ##########  LoanCost  ##########################

# ######## ADD Viwe  ##########  LoanCost  ##########################


@login_required
def addLoanCost(request, id, loanCostId=0):
    company = get_object_or_404(Company, pk=id)
    currency = Currency.objects.all()
    loanCost = LoanCost.objects.filter(company=id)
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    b = []
    for a in userAuthList:
        b.append(a.companyAuth.id)
    if id in b:
        if request.method == "GET":
            if loanCostId == 0:
                form = LoanCostForm()
            else:
                loanCost1 = LoanCost.objects.get(pk=loanCostId)
                form = LoanCostForm(instance=loanCost1)
            return render(request, 'budgeting/loancost.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'loanCost': loanCost, 'userAuth':b})
        else:
            if loanCostId == 0 :
                form = LoanCostForm(request.POST)
            else:
                loanCost1 = LoanCost.objects.get(pk=loanCostId)
                form = LoanCostForm(request.POST, instance=loanCost1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/loancost.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'loanCost': loanCost, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################


def calculateIncome(data,year):

    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + (c.realIncomeQ1 * currencyRate)
        x2 = x2 + c.realIncomeQ2 * currencyRate
        x3 = x3 + c.realIncomeQ3 * currencyRate
        x4 = x4 + c.realIncomeQ4 * currencyRate
        y1 = y1 + c.forcastIncomeQ1 * currencyRate
        y2 = y2 + c.forcastIncomeQ2 * currencyRate
        y3 = y3 + c.forcastIncomeQ3 * currencyRate
        y4 = y4 + c.forcastIncomeQ4 * currencyRate

    incomeData = {'realIncomeQ1': x1,
                  'realIncomeQ2': x1 + x2,
                  'realIncomeQ3': x1 + x2 + x3,
                  'realIncomeQ4': x1 + x2 + x3 + x4,
                  'forcastIncomeQ1': y1,
                  'forcastIncomeQ2': y1 + y2,
                  'forcastIncomeQ3': y1 + y2 + y3,
                  'forcastIncomeQ4': y1 + y2 + y3 + y4
                  }

    return incomeData

def calculateCostOfSale(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realCostQ1 * currencyRate
        x2 = x2 + c.realCostQ2 * currencyRate
        x3 = x3 + c.realCostQ3 * currencyRate
        x4 = x4 + c.realCostQ4 * currencyRate
        y1 = y1 + c.forcastCostQ1 * currencyRate
        y2 = y2 + c.forcastCostQ2 * currencyRate
        y3 = y3 + c.forcastCostQ3 * currencyRate
        y4 = y4 + c.forcastCostQ4 * currencyRate

    costOfSaleData = {'realCostQ1': x1,
                  'realCostQ2': x1 + x2,
                  'realCostQ3': x1 + x2 + x3,
                  'realCostQ4': x1 + x2 + x3 + x4,
                  'forcastCostQ1': y1,
                  'forcastCostQ2': y1 + y2,
                  'forcastCostQ3': y1 + y2 + y3,
                  'forcastCostQ4': y1 + y2 + y3 + y4
                  }

    return costOfSaleData

def calculatePublicCost(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realPublicCostQ1 * currencyRate
        x2 = x2 + c.realPublicCostQ2 * currencyRate
        x3 = x3 + c.realPublicCostQ3 * currencyRate
        x4 = x4 + c.realPublicCostQ4 * currencyRate
        y1 = y1 + c.forcastPublicCostQ1 * currencyRate
        y2 = y2 + c.forcastPublicCostQ2 * currencyRate
        y3 = y3 + c.forcastPublicCostQ3 * currencyRate
        y4 = y4 + c.forcastPublicCostQ4 * currencyRate

    publicCostData = {'realPublicCostQ1': x1,
                  'realPublicCostQ2': x1 + x2,
                  'realPublicCostQ3': x1 + x2 + x3,
                  'realPublicCostQ4': x1 + x2 + x3 + x4,
                  'forcastPublicCostQ1': y1,
                  'forcastPublicCostQ2': y1 + y2,
                  'forcastPublicCostQ3': y1 + y2 + y3,
                  'forcastPublicCostQ4': y1 + y2 + y3 + y4
                  }

    return publicCostData


def calculateEtcOprIcome(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realetcOprationIncomeQ1 * currencyRate
        x2 = x2 + c.realetcOprationIncomeQ2 * currencyRate
        x3 = x3 + c.realetcOprationIncomeQ3 * currencyRate
        x4 = x4 + c.realetcOprationIncomeQ4 * currencyRate
        y1 = y1 + c.forcastetcOprationIncomeQ1 * currencyRate
        y2 = y2 + c.forcastetcOprationIncomeQ2 * currencyRate
        y3 = y3 + c.forcastetcOprationIncomeQ3 * currencyRate
        y4 = y4 + c.forcastetcOprationIncomeQ4 * currencyRate

    etcOprIcomeData = {'realEtcOprationIncomeQ1': x1,
                       'realEtcOprationIncomeQ2': x1 + x2,
                       'realEtcOprationIncomeQ3': x1 + x2 + x3,
                       'realEtcOprationIncomeQ4': x1 + x2 + x3 + x4,
                       'forcastEtcOprationIncomeQ1': y1,
                       'forcastEtcOprationIncomeQ2': y1 + y2,
                       'forcastEtcOprationIncomeQ3': y1 + y2 + y3,
                       'forcastEtcOprationIncomeQ4': y1 + y2 + y3 + y4
                      }

    return etcOprIcomeData

def calculateEtcOprCost(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realEtcOprationCostQ1 * currencyRate
        x2 = x2 + c.realEtcOprationCostQ2 * currencyRate
        x3 = x3 + c.realEtcOprationCostQ3 * currencyRate
        x4 = x4 + c.realEtcOprationCostQ4 * currencyRate
        y1 = y1 + c.forcastEtcOprationCostQ1 * currencyRate
        y2 = y2 + c.forcastEtcOprationCostQ2 * currencyRate
        y3 = y3 + c.forcastEtcOprationCostQ3 * currencyRate
        y4 = y4 + c.forcastEtcOprationCostQ4 * currencyRate

    etcOprCostData = {'realEtcOprationCostQ1': x1,
                      'realEtcOprationCostQ2': x1 + x2,
                      'realEtcOprationCostQ3': x1 + x2 + x3,
                      'realEtcOprationCostQ4': x1 + x2 + x3 + x4,
                      'forcastEtcOprationCostQ1': y1,
                      'forcastEtcOprationCostQ2': y1 + y2,
                      'forcastEtcOprationCostQ3': y1 + y2 + y3,
                      'forcastEtcOprationCostQ4': y1 + y2 + y3 + y4
                      }

    return etcOprCostData


def calculateNonOprIncome(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realNonOprationIncomeQ1 * currencyRate
        x2 = x2 + c.realNonOprationIncomeQ2 * currencyRate
        x3 = x3 + c.realNonOprationIncomeQ3 * currencyRate
        x4 = x4 + c.realNonOprationIncomeQ4 * currencyRate
        y1 = y1 + c.forcastNonOprationIncomeQ1 * currencyRate
        y2 = y2 + c.forcastNonOprationIncomeQ2 * currencyRate
        y3 = y3 + c.forcastNonOprationIncomeQ3 * currencyRate
        y4 = y4 + c.forcastNonOprationIncomeQ4 * currencyRate

    nonOprIncomeData = {'realNonOprationIncomeQ1': x1,
                        'realNonOprationIncomeQ2': x1 + x2,
                        'realNonOprationIncomeQ3': x1 + x2 + x3,
                        'realNonOprationIncomeQ4': x1 + x2 + x3 + x4,
                        'forcastNonOprationIncomeQ1': y1,
                        'forcastNonOprationIncomeQ2': y1 + y2,
                        'forcastNonOprationIncomeQ3': y1 + y2 + y3,
                        'forcastNonOprationIncomeQ4': y1 + y2 + y3 + y4
                      }

    return nonOprIncomeData


def calculateNonOprCost(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realNonOprationCostQ1 * currencyRate
        x2 = x2 + c.realNonOprationCostQ2 * currencyRate
        x3 = x3 + c.realNonOprationCostQ3 * currencyRate
        x4 = x4 + c.realNonOprationCostQ4 * currencyRate
        y1 = y1 + c.forcastNonOprationCostQ1 * currencyRate
        y2 = y2 + c.forcastNonOprationCostQ2 * currencyRate
        y3 = y3 + c.forcastNonOprationCostQ3 * currencyRate
        y4 = y4 + c.forcastNonOprationCostQ4 * currencyRate

    nonOprCostData = {'realNonOprationCostQ1': x1,
                        'realNonOprationCostQ2': x1 + x2,
                        'realNonOprationCostQ3': x1 + x2 + x3,
                        'realNonOprationCostQ4': x1 + x2 + x3 + x4,
                        'forcastNonOprationCostQ1': y1,
                        'forcastNonOprationCostQ2': y1 + y2,
                        'forcastNonOprationCostQ3': y1 + y2 + y3,
                        'forcastNonOprationCostQ4': y1 + y2 + y3 + y4
                      }

    return nonOprCostData

def calculateTax(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realTaxQ1 * currencyRate
        x2 = x2 + c.realTaxQ2 * currencyRate
        x3 = x3 + c.realTaxQ3 * currencyRate
        x4 = x4 + c.realTaxQ4 * currencyRate
        y1 = y1 + c.forcastTaxQ1 * currencyRate
        y2 = y2 + c.forcastTaxQ2 * currencyRate
        y3 = y3 + c.forcastTaxQ3 * currencyRate
        y4 = y4 + c.forcastTaxQ4 * currencyRate

    taxData = {'realTaxQ1': x1,
               'realTaxQ2': x1 + x2,
               'realTaxQ3': x1 + x2 + x3,
               'realTaxQ4': x1 + x2 + x3 + x4,
               'forcastTaxQ1': y1,
               'forcastTaxQ2': y1 + y2,
               'forcastTaxQ3': y1 + y2 + y3,
               'forcastTaxQ4': y1 + y2 + y3 + y4
               }

    return taxData

def calculateLoanCost(data):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    for c in data:
        currency = c.currency
        currencyRate = currency.currencyRate
        x1 = x1 + c.realLoanCostQ1 * currencyRate
        x2 = x2 + c.realLoanCostQ2 * currencyRate
        x3 = x3 + c.realLoanCostQ3 * currencyRate
        x4 = x4 + c.realLoanCostQ4 * currencyRate
        y1 = y1 + c.forcastLoanCostQ1 * currencyRate
        y2 = y2 + c.forcastLoanCostQ2 * currencyRate
        y3 = y3 + c.forcastLoanCostQ3 * currencyRate
        y4 = y4 + c.forcastLoanCostQ4 * currencyRate

    loanCostData = {'realLoanCostQ1': x1,
               'realLoanCostQ2': x1 + x2,
               'realLoanCostQ3': x1 + x2 + x3,
               'realLoanCostQ4': x1 + x2 + x3 + x4,
               'forcastLoanCostQ1': y1,
               'forcastLoanCostQ2': y1 + y2,
               'forcastLoanCostQ3': y1 + y2 + y3,
               'forcastLoanCostQ4': y1 + y2 + y3 + y4
               }

    return loanCostData



@login_required
def benefitSheetCal(request, id, year):
    company = get_object_or_404(Company, pk=id)
    income = Income.objects.filter(company=id, yearOfForcast=year)
    costOfSales = CostOfSales.objects.filter(company=id, yearOfForcast=year)
    publicCost = PublicCost.objects.filter(company=id, yearOfForcast=year)
    etcOprIcome = EtcOprationalIncome.objects.filter(company=id, yearOfForcast=year)
    etcOprCost = EtcOprationalCost.objects.filter(company=id, yearOfForcast=year)
    nonOprIncome = NonOprationalIncome.objects.filter(company=id, yearOfForcast=year)
    nonOprCost = NonOprationalCost.objects.filter(company=id, yearOfForcast=year)
    tax = Tax.objects.filter(company=id, yearOfForcast=year)
    loanCost = LoanCost.objects.filter(company=id, yearOfForcast=year)
    incomeData = calculateIncome(income,year)
    costOfSalesData = calculateCostOfSale(costOfSales)
    publicCostData = calculatePublicCost(publicCost)
    etcOprIcomeData = calculateEtcOprIcome(etcOprIcome)
    etcOprCostData = calculateEtcOprCost(etcOprCost)
    nonOprIncomeData = calculateNonOprIncome(nonOprIncome)
    nonOprCostData = calculateNonOprCost(nonOprCost)
    taxData = calculateTax(tax)
    loanCostData = calculateLoanCost(loanCost)

    sood11 = incomeData['realIncomeQ1'] - costOfSalesData['realCostQ1']
    sood12 = incomeData['realIncomeQ2'] - costOfSalesData['realCostQ2']
    sood13 = incomeData['realIncomeQ3'] - costOfSalesData['realCostQ3']
    sood14 = incomeData['realIncomeQ4'] - costOfSalesData['realCostQ4']
    sood15 = incomeData['forcastIncomeQ1'] - costOfSalesData['forcastCostQ1']
    sood16 = incomeData['forcastIncomeQ2'] - costOfSalesData['forcastCostQ2']
    sood17 = incomeData['forcastIncomeQ3'] - costOfSalesData['forcastCostQ3']
    sood18 = incomeData['forcastIncomeQ4'] - costOfSalesData['forcastCostQ4']

    sood21 = sood11 - publicCostData['realPublicCostQ1']
    sood22 = sood12 - publicCostData['realPublicCostQ2']
    sood23 = sood13 - publicCostData['realPublicCostQ3']
    sood24 = sood14 - publicCostData['realPublicCostQ4']
    sood25 = sood15 - publicCostData['forcastPublicCostQ1']
    sood26 = sood16 - publicCostData['forcastPublicCostQ2']
    sood27 = sood17 - publicCostData['forcastPublicCostQ3']
    sood28 = sood18 - publicCostData['forcastPublicCostQ4']

    sood31 = sood21 + etcOprIcomeData['realEtcOprationIncomeQ1'] - etcOprCostData['realEtcOprationCostQ1']
    sood32 = sood22 + etcOprIcomeData['realEtcOprationIncomeQ2'] - etcOprCostData['realEtcOprationCostQ2']
    sood33 = sood23 + etcOprIcomeData['realEtcOprationIncomeQ3'] - etcOprCostData['realEtcOprationCostQ3']
    sood34 = sood24 + etcOprIcomeData['realEtcOprationIncomeQ4'] - etcOprCostData['realEtcOprationCostQ4']
    sood35 = sood25 + etcOprIcomeData['forcastEtcOprationIncomeQ1'] - etcOprCostData['forcastEtcOprationCostQ1']
    sood36 = sood26 + etcOprIcomeData['forcastEtcOprationIncomeQ2'] - etcOprCostData['forcastEtcOprationCostQ2']
    sood37 = sood27 + etcOprIcomeData['forcastEtcOprationIncomeQ3'] - etcOprCostData['forcastEtcOprationCostQ3']
    sood38 = sood28 + etcOprIcomeData['forcastEtcOprationIncomeQ4'] - etcOprCostData['forcastEtcOprationCostQ4']

    sood41 = sood21 + nonOprIncomeData['realNonOprationIncomeQ1'] - nonOprCostData['realNonOprationCostQ1']
    sood42 = sood22 + nonOprIncomeData['realNonOprationIncomeQ2'] - nonOprCostData['realNonOprationCostQ2']
    sood43 = sood23 + nonOprIncomeData['realNonOprationIncomeQ3'] - nonOprCostData['realNonOprationCostQ3']
    sood44 = sood24 + nonOprIncomeData['realNonOprationIncomeQ4'] - nonOprCostData['realNonOprationCostQ4']
    sood45 = sood25 + nonOprIncomeData['forcastNonOprationIncomeQ1'] - nonOprCostData['forcastNonOprationCostQ1']
    sood46 = sood26 + nonOprIncomeData['forcastNonOprationIncomeQ2'] - nonOprCostData['forcastNonOprationCostQ2']
    sood47 = sood27 + nonOprIncomeData['forcastNonOprationIncomeQ3'] - nonOprCostData['forcastNonOprationCostQ3']
    sood48 = sood28 + nonOprIncomeData['forcastNonOprationIncomeQ4'] - nonOprCostData['forcastNonOprationCostQ4']

    sood51 = sood41 - taxData['realTaxQ1']
    sood52 = sood42 - taxData['realTaxQ2']
    sood53 = sood43 - taxData['realTaxQ3']
    sood54 = sood44 - taxData['realTaxQ4']
    sood55 = sood45 - taxData['forcastTaxQ1']
    sood56 = sood46 - taxData['forcastTaxQ2']
    sood57 = sood47 - taxData['forcastTaxQ3']
    sood58 = sood48 - taxData['forcastTaxQ4']

    sood61 = sood51 - loanCostData['realLoanCostQ1']
    sood62 = sood52 - loanCostData['realLoanCostQ2']
    sood63 = sood53 - loanCostData['realLoanCostQ3']
    sood64 = sood54 - loanCostData['realLoanCostQ4']
    sood65 = sood55 - loanCostData['forcastLoanCostQ1']
    sood66 = sood56 - loanCostData['forcastLoanCostQ2']
    sood67 = sood57 - loanCostData['forcastLoanCostQ3']
    sood68 = sood58 - loanCostData['forcastLoanCostQ4']







    etcOfSheet = {'sood11': sood11, 'sood12': sood12, 'sood13': sood13, 'sood14': sood14, 'sood15': sood15,
                  'sood16': sood16, 'sood17': sood17, 'sood18': sood18,
                  'sood21': sood21, 'sood22': sood22, 'sood23': sood23, 'sood24': sood24, 'sood25': sood25,
                  'sood26': sood26, 'sood27': sood27, 'sood28': sood28,
                  'sood31': sood31, 'sood32': sood32, 'sood33': sood33, 'sood34': sood34, 'sood35': sood35,
                  'sood36': sood36, 'sood37': sood37, 'sood38': sood38,
                  'sood41': sood41, 'sood42': sood42, 'sood43': sood43, 'sood44': sood44, 'sood45': sood45,
                  'sood46': sood46, 'sood47': sood47, 'sood48': sood48,
                  'sood51': sood51, 'sood52': sood52, 'sood53': sood53, 'sood54': sood54, 'sood55': sood55,
                  'sood56': sood56, 'sood57': sood57, 'sood58': sood58,
                  'sood61': sood61, 'sood62': sood62, 'sood63': sood63, 'sood64': sood64, 'sood65': sood65,
                  'sood66': sood66, 'sood67': sood67, 'sood68': sood68
                  }

    return  render(request, 'budgeting/sheet.html', {'incomdata': incomeData,
                                                     'costOfSalesData': costOfSalesData,
                                                     'publicCostData' : publicCostData,
                                                     'etcOprIcomeData' : etcOprIcomeData,
                                                     'etcOprCostData' : etcOprCostData,
                                                     'nonOprIncomeData' : nonOprIncomeData,
                                                     'nonOprCostData' : nonOprCostData,
                                                     'taxData' : taxData,
                                                     'loanCostData' : loanCostData,
                                                     'etcOfSheet' : etcOfSheet,
                                                     'companies': company })

