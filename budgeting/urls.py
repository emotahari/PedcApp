from . import views
from django.urls import path

app_name = 'budgeting'
urlpatterns = [
    path('income/', views.income_view, name='income'),


]