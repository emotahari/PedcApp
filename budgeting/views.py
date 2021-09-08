from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from accounts.models import Company, ProfileAuth
from budgeting.forms import IncomeAdd, CostAddShow, PublicCostForm, EtcOprationlIncomeForm, EtcOprationlCostForm, \
    NonOprationlIncometForm, NonOprationlCostForm, TaxForm, LoanCostForm
from budgeting.models import Income, Currency, CostType, CostOfSales, PublicCostType, PublicCost, EtcOprationalIncome, \
    EtcOprationalCost, NonOprationalIncome, NonOprationalCost, Tax, LoanCost


#  incomAdd
@login_required
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

@login_required
def delete_income_data(request, id):
    if request.method == 'POST':
        deleted_income = Income.objects.get(pk=id)
        companyid = deleted_income.company.id
        deleted_income.delete()
    return redirect('budgeting:income', companyid)
    # return redirect(income_view(request, company_id=Income.company.id))

    # income edit

@login_required
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
                tax1 = LoanCost.objects.get(pk=loanCostId)
                form = LoanCostForm(instance=tax1)
            return render(request, 'budgeting/loancost.html', {'form': form, 'companies': company, 'currency': currency
                                                          , 'loanCost': loanCost, 'userAuth':b})
        else:
            if loanCostId == 0 :
                form = LoanCostForm(request.POST)
            else:
                tax1 = LoanCost.objects.get(pk=loanCostId)
                form = LoanCostForm(request.POST, instance=tax1)
            if form.is_valid():
                form.save()
            return render(request, 'budgeting/loancost.html', {'form': form, 'companies': company, 'currency': currency
                                                          ,'loanCost': loanCost, 'userAuth':b})
    else:
        return HttpResponseRedirect(reverse('accounts:companyList'))



# ########################  END  #######################################
