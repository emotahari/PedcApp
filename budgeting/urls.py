from . import views
from django.urls import path

app_name = 'budgeting'
urlpatterns = [
    path('income/<int:company_id>', views.income_view, name='income'),


]