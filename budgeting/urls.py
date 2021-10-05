from . import views
from django.urls import path

app_name = 'budgeting'
urlpatterns = [
    path('income/<int:company_id>', views.income_view, name='income'),
    path('modal/<int:id>', views.delete_income_data, name='modal'),
    path('updateincome/<int:incomeId>', views.update_income_data, name='updateincome'),
    path('cost/<int:id>', views.addCostOfSales, name='costofsale'),
    path('cost/<int:id>/<int:costid>', views.addCostOfSales, name='updatecostofsale'),
    path('cost/<int:id>', views.delete_income_data, name='deletecost'),
    path('publiccost/<int:id>', views.addPublicCost, name='publiccost'),
    path('etcoprincome/<int:id>', views.addEtcOprationlIncome, name='etcoprincome'),
    path('etcoprcost/<int:id>', views.addEtcOprationalCost, name='etcoprcost'),
    path('nonoprincome/<int:id>', views.addNonOprationalIncome, name='nonoprincome'),
    path('nonoprcost/<int:id>', views.addNonOprationalCost, name='nonoprcost'),
    path('tax/<int:id>', views.addTax, name='tax'),
    path('loancost/<int:id>', views.addLoanCost, name='loancost'),
    path('sheet/<int:id>/<int:year>', views.benefitSheetCal, name='sheet'),



]
