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
    address =models.CharField()
    profilePhoto = models.ImageField()
    accountName  = models.CharField(max_length=15)
    balance = models.DecimalField()
    status = models.CharField()
    bankAccountName = models.CharField()
    bankAccountNumber = models.CharField()
    userName = models.CharField(max_length=15)
    userEmail = models.EmailField()
    transaction = models.DecimalField()
    userPhoneNumber = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    time = models.DateTimeField()
    userId = models.BigAutoField()
    customer = models.OneToOneField()
    pin = models.SmallIntegerField()
    isActive = models.BooleanField()


class Account(models.Model):
    account = models.CharField()
    balance = models.PositiveIntegerField()
    name = models.CharField(max_length=15)


class Transaction(models.Model):
    accountName  = models.CharField()
    accountOrigin = models.ForeignKey()
    accountNumber = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    currency = models.CharField()
    location = models.CharField()
    destination = models.ForeignKey()
    status  = models.CharField()
    date = models.DateTimeField()
    thirdParty = models.CharField()


class Card(models.Model):
    cardholderNumber = models.CharField()
    cardHolderName = models.CharField()
    expiryDate = models.DateTimeField()
    cVVSecurityCode = models.PositiveSmallIntegerField()
    cardStatus = models.CharField()
    signature  = models.ImageField()
    issuer = models.CharField()




class ThirdParty(models.Model):
    accountName = models.CharField()
    accountNumber = models.BigAutoField()
    amount = models.PositiveIntegerField()
    currency = models.CharField()
    location  = models.CharField()
    transactionCost = models.PositiveIntegerField()
    isActive = models.BooleanField()


class Notification(models.Model):
    message = models.CharField()
    title = models.CharField()
    isActive = models.CharField()
    recipient = models.ForeignKey()
    date = models.DateTimeField()


class Receipt(models.Model):
    receiptType = models.CharField()
    receiptDate = models.DateTimeField()
    billNumber = models.BigAutoField()
    date = models.DateTimeField()
    transaction = models.ForeignKey()
    file = models.FilePathField()


class Loan(models.Model):
    amount  = models.PositiveIntegerField()
    loanType = models.CharField()
    loanId = models.CharField()
    loanID = models.BigAutoField()
    amount = models.BigAutoField()
    date = models.DateTimeField()
    status = models.CharField()
    dulationMonths = models.CharField()
    paymentDueDate  = models.DateTimeField()



class Reward(models.Model):
    Gender = models.CharField(max_length=1)
    Name = models.CharField(max_length=15)
    CustomerID = models.BigAutoField
    Wallet = models.ForeignKey
    Transaction = models.ForeignKey


