from django import forms
from .models import Card, Customer, Receipt, Wallet, Account, Transaction, Card, ThirdParty, Notification, Loan, Reward

# what are the content of http class

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

# Create your views here.
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = "__all__"
class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"

# class ReceiptRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Receipt
#         fields = "__all__"

