from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def income_view(request):
    return HttpResponseRedirect(reverse('budgeting:income'))