from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.source} - Ksh{self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.category} - Ksh{self.amount}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - Ksh{self.amount}"











