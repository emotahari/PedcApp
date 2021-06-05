from . import views
from django.urls import path

from .views import company_view

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('company/companylist/', company_view, name="companyList"),
    path('company/details/<int:company_id>', company_view, name="companyDetails")

]
