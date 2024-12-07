from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Budget
from .forms import IncomeForm, ExpenseForm, BudgetForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

@login_required
def dashboard(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    budgets = Budget.objects.filter(user=request.user)
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    remaining_budget = sum(budget.amount for budget in budgets) - total_expense
    return render(request, 'index.html', {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'remaining_budget': remaining_budget,
    })

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', {'form': form})

@login_required
def add_expense(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expense = sum(expense.amount for expense in expenses)
    budgets = Budget.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
        if total_expense > sum(budget.amount for budget in budgets):
            send_mail(
                'Budget Exceeded',
                'You have exceeded your budget!',
                settings.EMAIL_HOST_USER,
                [request.user.email],
            )

    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('home')
    else:
        form = BudgetForm()
    return render(request, 'add_budget.html', {'form': form})

def update_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, "Income updated successfully!")
            return redirect('home')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'update_income.html', {'form': form})

# Update Expense
def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated successfully!")
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'update_expense.html', {'form': form})

# Update Budget
def update_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            messages.success(request, "Budget updated successfully!")
            return redirect('home')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'update_budget.html', {'form': form})

# Delete Views
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        messages.success(request, "Income deleted successfully!")
        return redirect('home')
    return render(request, 'delete_confirm.html', {'object': income, 'type': 'Income'})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, "Expense deleted successfully!")
        return redirect('dashboard')
    return render(request, 'delete_confirm.html', {'object': expense, 'type': 'Expense'})

def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        budget.delete()
        messages.success(request, "Budget deleted successfully!")
        return redirect('home')
    return render(request, 'delete_confirm.html', {'object': budget, 'type': 'Budget'})






