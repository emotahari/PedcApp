from . import views
from django.urls import path

app_name = 'budgeting'
urlpatterns = [
    path('income/<int:company_id>', views.income_view, name='income'),
    path('deleteincome/<int:id>', views.delete_income_data, name='deleteincome'),
    path('updateincome/<int:incomeId>', views.update_income_data, name='updateincome'),
    path('cost/<int:id>', views.addCostOfSales, name='costofsale'),
    path('cost/<int:id>/<int:costid>', views.addCostOfSales, name='updatecostofsale'),
    path('deletecost/<int:id>', views.delete_costOfSale_data, name='deletecost'),
    path('publiccost/<int:id>', views.addPublicCost, name='publiccost'),
    path('delpubliccost/<int:id>', views.delete_PublicCost_data, name='publiccostdel'),
    path('etcoprincome/<int:id>', views.addEtcOprationlIncome, name='etcoprincome'),
    path('deletcoprincome/<int:id>', views.delete_etcOprIn_data, name='etcoprincomedel'),
    path('etcoprcost/<int:id>', views.addEtcOprationalCost, name='etcoprcost'),
    path('deletcoprcost/<int:id>', views.delete_etcOprCost_data, name='etcoprcostdel'),
    path('nonoprincome/<int:id>', views.addNonOprationalIncome, name='nonoprincome'),
    path('delnonoprincome/<int:id>', views.delete_nonOprIn_data, name='nonoprincomedel'),
    path('nonoprcost/<int:id>', views.addNonOprationalCost, name='nonoprcost'),
    path('delnonoprcost/<int:id>', views.delete_nonOprCost_data, name='nonoprcostdel'),
    path('tax/<int:id>', views.addTax, name='tax'),
    path('deltax/<int:id>', views.delete_tax, name='taxdel'),
    path('loancost/<int:id>', views.addLoanCost, name='loancost'),
    path('delloancost/<int:id>', views.delete_LoanCost, name='loancostdel'),
    path('sheet/<int:id>/<int:year>', views.benefitSheetCal, name='sheet'),
    path('crrntasst/<int:id>', views.AddCrntAsst, name='crrntasst'),
    path('ncrrntasst/<int:id>', views.AddNCrntAsst, name='ncrrntasst'),
    path('crrntlblt/<int:id>', views.AddCrntLblt, name='crrntlblt'),
    path('ncrrntlblt/<int:id>', views.AddNCrntLblt, name='ncrrntlblt'),
    path('prprtyrght/<int:id>', views.AddPrprtyRights, name='prprtyRights'),
    path('cmpnydashh/<int:id>', views.CompnyDash, name='cmpnydash'),
    path('balancsheet/<int:id>', views.BalanceSheetCal, name='balancesheet'),



]
