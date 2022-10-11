from rest_framework import viewsets
from wallet.models import Customer
from ..Api.serializers import CustomerSerializer, WalletSerializer, AccountSerializer, CardSerializer, TransactionSerializer, NotificationSerializer, LoanSerializer
from django.shortcuts import render, redirect
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .forms import CustomerRegistrationForm, WalletRegistrationForm, AccountRegistrationForm, TransactionRegistrationForm, CardRegistrationForm, ThirdPartyRegistrationForm,NotificationRegistrationForm, LoanRegistrationForm, RewardRegistrationForm

class CustomerViewset(viewsets.ModelViewset):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()

    return render(request, "wallet/register_customer.html",{"form": form})
        
class WalletViewset(viewsets.ModelViewset):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

def register_wallet(request):
    # form = WalletRegistrationForm()
    # return render(request, "wallet/register_wallet.html",{"form": form})
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()

    return render(request, "wallet/register_customer.html",{"form": form})
  
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "wallet/list_customer.html", {"customers":customers})

def customer_profile(request, id):
    customer= Customer.objects.get(id= id)
    return render(request, "wallet/customer_profile.html", {"customer": customer})

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        form  = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id= customer.id)
    else:
        form = CustomerRegistrationForm(instance=customer)
        return render(request, "wallet/edit_customer.html", {"form": form})
        



def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()
        
    return render(request, "wallet/register_wallet.html",{"form": form})

def list_wallets(request):
    wallets = Wallet.objects.all()
    return render(request, "wallet/list_wallet.html", {"wallets":wallets})

def wallet_profile(request, id):
    wallet= Wallet.objects.get(id= id)
    return render(request, "wallet/wallet_profile.html", {"wallet": wallet})

def edit_wallet(request, id):
    wallet = Wallet.objects.get(id= id)
    if request.method=="POST":
        form  = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile", id= wallet.id)
    else:
        form = WalletRegistrationForm(instance=wallet)
        return render(request, "wallet/edit_wallet.html", {"form": form})



class AccountViewset(viewsets.ModelViewset):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    
def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()
        
    return render(request, "wallet/register_account.html",{"form": form})

def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, "wallet/list_account.html", {"accounts":accounts})

def account_profile(request, id):
    account= Account.objects.get(id= id)
    return render(request, "wallet/account_profile.html", {"account": account})

def edit_account(request, id):
    account = Account.objects.get(id=id)
    if request.method=="POST":
        form  = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile", id= account.id)
    else:
        form = WalletRegistrationForm(instance=account)
        return render(request, "wallet/edit_account.html", {"form": form})



class TransactionViewset(viewsets.ModelViewset):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()

    return render(request, "wallet/register_transaction.html",{"form": form})
  
def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "wallet/list_transaction.html", {"transactions":transactions})

def transaction_profile(request, id):
    transaction= Transaction.objects.get(id= id)
    return render(request, "wallet/transaction_profile.html", {"transaction": transaction})

def edit_transaction(request, id):
    transaction = Transaction.objects.get(id=id)
    if request.method=="POST":
        form  = TransactionRegistrationForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile", id= transaction.id)
    else:
        form = TransactionRegistrationForm(instance=transaction)
        return render(request, "wallet/edit_transaction.html", {"form": form})
        
    # form = TransactionRegistrationForm()
    # return render(request, "wallet/register_transaction.html",{"form": form})


class CardViewset(viewsets.ModelViewset):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()

    return render(request, "wallet/register_card.html",{"form": form})

def list_cards(request):
    cards = Card.objects.all()
    return render(request, "wallet/list_card.html", {"cards":cards})

def card_profile(request, id):
    card= Card.objects.get(id= id)
    return render(request, "wallet/card_profile.html", {"card": card})

def edit_card(request, id):
    card = Card.objects.get(id=id)
    if request.method=="POST":
        form  = CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_profile", id= card.id)
    else:
        form = CardRegistrationForm(instance=card)
        return render(request, "wallet/edit_card.html", {"form": form})
        
    # form = CardRegistrationForm()
    # return render(request, "wallet/register_card.html",{"form": form})


def register_thirdParty(request):
    if request.method == "POST":
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdPartyRegistrationForm()

    return render(request, "wallet/register_thirdParty.html",{"form": form})
  
def list_thirdPartys(request):
    thirdPartys = ThirdParty.objects.all()
    return render(request, "wallet/list_thirdParty.html", {"thirdPartys":thirdPartys})

def thirdParty_profile(request, id):
    thirdParty= ThirdParty.objects.get(id= id)
    return render(request, "wallet/thirdParty_profile.html", {"thirdParty": thirdParty})

def edit_thirdParty(request, id):
    thirdParty = ThirdParty.objects.get(id=id)
    if request.method=="POST":
        form  = ThirdPartyRegistrationForm(request.POST, instance=thirdParty)
        if form.is_valid():
            form.save()
            return redirect("thirdParty_profile", id= thirdParty.id)
    else:
        form = ThirdPartyRegistrationForm(instance=thirdParty)
        return render(request, "wallet/edit_thirdParty.html", {"form": form})
        
    # form = ThirdPartyRegistrationForm()
    # return render(request, "wallet/register_thirdParty.html",{"form": form})


class NotificationViewset(viewsets.ModelViewset):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()

    return render(request, "wallet/register_notification.html",{"form": form})
  
def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request, "wallet/list_notification.html", {"notifications":notifications})

def notification_profile(request, id):
    notification= Notification.objects.get(id= id)
    return render(request, "wallet/notification_profile.html", {"notification": notification})

def edit_notification(request, id):
    notification = Notification.objects.get(id=id)
    if request.method=="POST":
        form  = NotificationRegistrationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id= notification.id)
    else:
        form = NotificationRegistrationForm(instance=notification)
        return render(request, "wallet/edit_notification.html", {"form": form})
        
    # form = NotificationRegistrationForm()
    # return render(request, "wallet/register_notification.html",{"form": form})


class LoanViewset(viewsets.ModelViewset):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()

    return render(request, "wallet/register_loan.html",{"form": form})
  
def list_loans(request):
    loans = Loan.objects.all()
    return render(request, "wallet/list_loan.html", {"loans":loans})

def loan_profile(request, id):
    loan= Loan.objects.get(id= id)
    return render(request, "wallet/loan_profile.html", {"loan": loan})

def edit_loan(request, id):
    loan = Loan.objects.get(id=id)
    if request.method=="POST":
        form  = LoanRegistrationForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect("loan_profile", id= loan.id)
    else:
        form = LoanRegistrationForm(instance=loan)
        return render(request, "wallet/edit_loan.html", {"form": form})
        
    # form = LoanRegistrationForm()
    # return render(request, "wallet/register_loan.html",{"form": form})



def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RewardRegistrationForm()

    return render(request, "wallet/register_reward.html",{"form": form})
  
def list_rewards(request):
    rewards = Reward.objects.all()
    return render(request, "wallet/list_reward.html", {"rewards":rewards})

def reward_profile(request, id):
    reward= Reward.objects.get(id= id)
    return render(request, "wallet/reward_profile.html", {"reward": reward})

def edit_reward(request, id):
    reward = Reward.objects.get(id=id)
    if request.method=="POST":
        form  = RewardRegistrationForm(request.POST, instance=reward)
        if form.is_valid():
            form.save()
            return redirect("reward_profile", id= reward.id)
    else:
        form = RewardRegistrationForm(instance=reward)
        return render(request, "wallet/edit_reward.html", {"form": form})
        
    # form = RewardRegistrationForm()
    # return render(request, "wallet/register_reward.html",{"form": form})




# def register_receipt(request):
#     if request.method == "POST":
#         form = ReceiptRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ReceiptRegistrationForm()

#     return render(request, "wallet/register_receipt.html",{"form": form})
  
# def list_receipts(request):
#     receipts = Receipt.objects.all()
#     return render(request, "wallet/list_receipt.html", {"receipts":receipts})

# def receipt_profile(request, id):
#     receipt= Receipt.objects.get(id= id)
#     return render(request, "wallet/receipt_profile.html", {"receipt": receipt})

# def edit_receipt(request, id):
#     receipt = Receipt.objects.get(id=id)
#     if request.method=="POST":
#         form  = ReceiptRegistrationForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect("receipt_profile", id= receipt.id)
#     else:
#         form = ReceiptRegistrationForm(instance=receipt)
#         return render(request, "wallet/edit_receipt.html", {"form": form})
        
    # form = ReceiptRegistrationForm()
    # return render(request, "wallet/register_receipt.html",{"form": form})




