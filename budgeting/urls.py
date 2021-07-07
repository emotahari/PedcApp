from . import views
from django.urls import path

app_name = 'budgeting'
urlpatterns = [
    path('income/<int:company_id>', views.income_view, name='income'),
    path('deleteincome/<int:id>', views.delete_income_data, name='deleteincome'),
    path('updateincome/<int:incomeId>', views.update_income_data, name='updateincome'),
    path('cost/<int:id>', views.addCostOfSales, name='costofsale'),
    path('cost/<int:id>/<int:costid>', views.addCostOfSales, name='updatecostofsale'),
    path('cost/<int:id>', views.delete_income_data, name='deletecost'),

]