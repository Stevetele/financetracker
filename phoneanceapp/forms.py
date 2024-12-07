from django import forms
from .models import Income, Expense, Budget

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'date']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'start_date', 'end_date']

