from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import accounts
from accounts.models import Company, ProfileAuth


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                'username': username
            }
            return HttpResponseRedirect(reverse('accounts:companyList'))
        else:
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد'
            }
            # raise Http404("نام کاربری و یا رمز عبور نادرست است")

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:companyList'))
        context = {}
    return render(request, 'accounts/login.html', context)


    # else:
    #     return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def company_view(request):
    userAuth = request.user
    userAuthList = ProfileAuth.objects.filter(userAuth=userAuth)
    authCompanyId = []
    companyList =[]
    for i in userAuthList:
        if i.companyAuth.id not in authCompanyId:
            authCompanyId.append(i.companyAuth.id)

    for j in authCompanyId:
        companyinstance = Company.objects.get(id=j)
        companyList.append(companyinstance)
    context = {
        'company_list' : companyList
    }
    return render(request, 'accounts/companylist.html', context)
