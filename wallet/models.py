from locale import currency
from statistics import mode
from django.db import models

# Create your models here.
class Customer (models.Model):
    firstname = models.CharField(max_length=15)
    secondname  = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=15)
    email = models.EmailField()


class Wallet(models.Model):
    Address =models.CharField
    ProfilePhoto = models.ImageField
    AccountName  = models.CharField(max_length=15)
    Balance = models.DecimalField
    Status = models.CharField
    BankAccountName = models.CharField
    BankAccountNumber = models.CharField
    UserName = models.CharField(max_length=15)
    UserEmail = models.EmailField
    Transaction = models.DecimalField
    UserPhoneNumber = models.PositiveIntegerField
    Amount = models.PositiveIntegerField
    Time = models.DateTimeField
    UserId = models.BigAutoField
    Customer = models.OneToOneField
    Pin = models.SmallIntegerField
    IsActive = models.BooleanField


class Account(models.Model):
    Account = models.CharField
    Balance = models.PositiveIntegerField
    Name = models.CharField(max_length=15)


class Transaction(models.Model):
    AccountName  = models.CharField
    AccountOrigin = models.ForeignKey
    AccountNumber = models.PositiveIntegerField
    Amount = models.PositiveIntegerField
    Currency = models.CharField
    Location = models.CharField
    Destination = models.ForeignKey
    Status  = models.CharField
    Date = models.DateTimeField
    ThirdParty = models.CharField


class Card(models.Model):
    CardholderNumber = models.CharField
    CardHolderName = models.CharField
    ExpiryDate = models.DateTimeField
    CVVSecurityCode = models.PositiveSmallIntegerField
    CardStatus = models.CharField
    Signature  = models.ImageField
    Issuer = models.CharField




class ThirdParty(models.Model):

    AccountName = models.CharField
    AccountNumber = models.BigAutoField
    Amount = models.BigAutoField
    Currency = models.CharField
    Location  = models.CharField
    TransactionCost = models.PositiveIntegerField
    IsActive = models.BooleanField


class Notification(models.Model):

    Message = models.CharField
    Title = models.CharField
    IsActive = models.CharField
    Recipient = models.ForeignKey
    Date = models.DateTimeField


class Receipt(models.Model):

    ReceiptType = models.CharField
    ReceiptDate = models.DateTimeField
    BillNumber = models.BigAutoField
    Date = models.DateTimeField
    Transaction = models.ForeignKey
    File = models.FilePathField


class Loan(models.Model):
    Amount  = models.PositiveIntegerField
    LoanType = models.CharField
    LoanId = models.CharField
    LoanID = models.BigAutoField
    Amount = models.BigAutoField
    Date = models.DateTimeField
    Status = models.CharField
    DulationMonths = models.CharField
    PaymentDueDate  = models.DateTimeField



class Reward(models.Model):

    Gender = models.CharField(max_length=1)
    Name = models.CharField(max_length=15)
    CustomerID = models.BigAutoField
    Wallet = models.ForeignKey
    Transaction = models.ForeignKey


