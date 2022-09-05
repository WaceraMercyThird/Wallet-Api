# from concurrent.futures.process import _ThreadWakeup
from datetime import datetime
# from distutils.command.upload import upload
from django.db import models
# from sqlalchemy import true

# Create your models here.
class Customer (models.Model):
    first_name = models.CharField(max_length=15,null=True)
    last_name  = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=1, null=True)
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=15,null=True)
    email = models.EmailField()


class Wallet(models.Model):
    customer = models.OneToOneField("customer", on_delete=models.CASCADE)
    balance = models.IntegerField()
    user_name = models.CharField(max_length=15, null=True)
    time = models.DateTimeField(default=datetime.now)
    pin = models.SmallIntegerField()
    is_active = models.BooleanField()
    type =models.CharField(max_length=15)
    


class Account(models.Model):
    account = models.CharField(max_length=15)
    balance = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=15, )


class Transaction(models.Model):
    account_name  = models.CharField(max_length=12, null=True)
    account_number = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=10)
    location = models.CharField(max_length=15)
    status  = models.CharField(max_length=10, null=True)
    date = models.DateTimeField(default=datetime.now)
    third_party = models.CharField(max_length=20, null=True)
    transaction_code = models.CharField(max_length=15, null= True)


class Card(models.Model):
    
    card_number = models.CharField(max_length=20, default=False, blank=True)
    card_name = models.CharField(max_length=12,null=True)
    expiry_date = models.DateTimeField(default=datetime.now)
    cVV_security_code = models.PositiveSmallIntegerField(default=0)
    card_status = models.CharField(max_length=15,default=False, blank=True)
    signature  = models.ImageField(upload_to='signature', null=True)
    issuer = models.CharField(max_length=15,default=False, blank=True)
    account_number = models.PositiveIntegerField()


class ThirdParty(models.Model):
    account_name = models.CharField(max_length=20, null=True)
    account_number = models.PositiveBigIntegerField()
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=20, null=True)
    location  = models.CharField(max_length=20, null=True)
    transaction_cost = models.PositiveIntegerField()
    is_Active = models.BooleanField(default=True)


class Notification(models.Model):
    message = models.CharField(max_length=20,null=True)
    title = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)


class Receipt(models.Model):
    receipt_type = models.CharField(max_length=15,null=True)
    receipt_date = models.DateTimeField(default=datetime.now)
    bill_number = models.PositiveBigIntegerField()
    date = models.DateTimeField(default=datetime.now)
    file = models.FilePathField()


class Loan(models.Model):
    loan_id = models.CharField(max_length=15)
    amount = models.PositiveBigIntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=15)
    dulation_months = models.CharField(max_length=10,null=True)
    payment_due_date  = models.DateTimeField(default=datetime.now)


class Reward(models.Model):
    name = models.CharField(max_length=15,null=True)
    transaction = models.ForeignKey('transaction',on_delete=models.CASCADE,related_name='Reward_transaction')
    date = models.DateTimeField(default=datetime.now)


