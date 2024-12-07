from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard, name='home'),

    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-budget/', views.add_budget, name='add_budget'),
    path('update-income/<int:pk>/', views.update_income, name='update_income'),
    path('update-expense/<int:pk>/', views.update_expense, name='update_expense'),
    path('update-budget/<int:pk>/', views.update_budget, name='update_budget'),
    path('delete-income/<int:pk>/', views.delete_income, name='delete_income'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('delete-budget/<int:pk>/', views.delete_budget, name='delete_budget'),



]