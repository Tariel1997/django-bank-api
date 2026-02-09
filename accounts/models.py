from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class BankAccount(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="bank_account"
    )
    balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0.00")
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Account - Balance: ${self.balance}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("DEPOSIT", "Deposit"),
        ("WITHDRAWAL", "Withdrawal"),
        ("TRANSFER_IN", "Transfer In"),
        ("TRANSFER_OUT", "Transfer Out"),
    ]

    CATEGORY_CHOICES = [
        ("FOOD", "Food & Drinks"),
        ("TRANSPORT", "Transport"),
        ("BILLS", "Utilities/Bills"),
        ("SHOPPING", "Shopping"),
        ("SALARY", "Salary"),
        ("OTHER", "Other"),
    ]

    account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="OTHER"
    )
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount} on {self.created_at.strftime('%Y-%m-%d')}"
