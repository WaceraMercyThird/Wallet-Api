from concurrent.futures.process import _ThreadWakeup
from datetime import datetime
from distutils.command.upload import upload
from locale import currency
from statistics import mode
from wsgiref.simple_server import demo_app
from django.db import models
from sqlalchemy import true

# Create your models here.
class Customer (models.Model):
    firstname = models.CharField(max_length=15,null=True)
    secondname  = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=1, null=True)
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=15,null=True)
    email = models.EmailField()


class Wallet(models.Model):
    address =models.CharField(max_length=20,null=True)
    profile_Photo = models.ImageField(upload_to='profile_Photo', null=True)
    accountName  = models.CharField(max_length=15,null=True)
    balance = models.DecimalField(decimal_places=2,)
    status = models.CharField(max_length=20)
    bankAccountName = models.CharField(max_length=15)
    bankAccountNumber = models.CharField(max_length=20)
    userName = models.CharField(max_length=15)
    userEmail = models.EmailField()
    transaction = models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Reward_transaction')
    userPhoneNumber = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    time = models.DateTimeField(default=datetime.now)
    userId = models.PositiveBigIntegerField()
    pin = models.SmallIntegerField()
    is_Active = models.BooleanField(default=False)


class Account(models.Model):
    account = models.CharField()
    balance = models.PositiveIntegerField()
    name = models.CharField(max_length=15, null=True)


class Transaction(models.Model):
    accountName  = models.CharField()
    accountType = models.ForeignKey('account_Type',on_delete=models.CASCADE,related_name='Reward_account_Type')
    accountNumber = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=10)
    location = models.CharField()
    destination = models.ForeignKey('destination',on_delete=models.CASCADE,related_name='Reward_destination')
    status  = models.CharField(max_length=10, null=True)
    date = models.DateTimeField(default=datetime.now)
    thirdParty = models.CharField(max_length=20, null=True)


class Card(models.Model):
    cardholderNumber = models.CharField()
    cardHolderName = models.CharField()
    expiryDate = models.DateTimeField(default=datetime.now)
    cVVSecurityCode = models.PositiveSmallIntegerField()
    cardStatus = models.CharField()
    signature  = models.ImageField(upload_to='signature', null=True)
    issuer = models.CharField()




class ThirdParty(models.Model):
    accountName = models.CharField(max_length=20, null=True)
    accountNumber = models.PositiveBigIntegerField()
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=20, null=True)
    location  = models.CharField(max_length=20, null=True)
    transactionCost = models.PositiveIntegerField()
    is_Active = models.BooleanField(default=True)


class Notification(models.Model):
    message = models.CharField()
    title = models.CharField()
    is_Active = models.BooleanField(default=False)
    recipient = models.ForeignKey('recipient',on_delete=models.CASCADE,related_name='Reward_recipient')
    date = models.DateTimeField(default=datetime.now)


class Receipt(models.Model):
    receiptType = models.CharField(max_length=15, null=True)
    receiptDate = models.DateTimeField(default=datetime.now)
    billNumber = models.PositiveBigIntegerField(max_length=15,null=True)
    date = models.DateTimeField(default=datetime.now)
    transaction = models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Reward_transaction')
    file = models.FilePathField()


class Loan(models.Model):
    amount  = models.PositiveIntegerField()
    loan_Type = models.CharField()
    loan_Id = models.CharField()
    loan_Id = models.PositiveBigIntegerField()
    amount = models.PositiveBigIntegerField()
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField()
    dulation_Months = models.CharField(max_length=10,null=True)
    paymentDueDate  = models.DateTimeField(default=datetime.now)



class Reward(models.Model):
    gender = models.CharField(("M", "Male"),("F","Famale"))
    name = models.CharField(max_length=15,null=True)
    customerID = models.BigAutoField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Reward_wallet')
    transaction = models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Reward_transaction')


