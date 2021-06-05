from . import views
from django.urls import path

app_name = 'budjeting'
urlpatterns = [
    path('income/', views.income_view, name='income'),


]