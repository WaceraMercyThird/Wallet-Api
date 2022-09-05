from encodings import search_function
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)
    search_fields= ("first_name", "last_name",)
admin.site.register(Customer, CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
   list_display = ("user_name", "customer", "balance",)
   search_fields= ("user_name", "customer",)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
   list_display = ("name", "account", "balance",)
   search_fields= ("name", "account",)
admin.site.register(Account, AccountAdmin)
 
class TransactionAdmin(admin.ModelAdmin):
   list_display = ("account_name", "account_no", "transaction_code",)
   search_fields= ("account_name", "account_no",)
admin.site.register(Transaction,)
 
class CardAdmin(admin.ModelAdmin):
   list_display = ("account_number","card_number", "card_name",)
   search_fields= ("account_number", "card_number",)
admin.site.register(Card, CardAdmin)
 
class ThirdPartyAdmin(admin.ModelAdmin):
   list_display = ("account_name", "account_number", "amount",)
   search_fields= ("account_name", "account_number",)
admin.site.register(ThirdParty,ThirdPartyAdmin)
 
class NotificationAdmin(admin.ModelAdmin):
   list_display = ("title", "message", "date",)
   search_fields= ("title", "message",)
admin.site.register(Notification, NotificationAdmin)
 
class ReceiptAdmin(admin.ModelAdmin):
   list_display = ("receipt_type", "receipt_date", "bill_number",)
   search_fields= ("receipt_type", "receipt_date",)
admin.site.register(Receipt, ReceiptAdmin)
 
class LoanAdmin(admin.ModelAdmin):
   list_display = ("loan_id", "amount", "date",)
   search_fields= ("loan_id", "amount",)
admin.site.register(Loan,LoanAdmin)
 
class RewardAdmin(admin.ModelAdmin):
   list_display = ("name", "date", "transaction")
   search_fields= ("name", "date",)
admin.site.register(Reward,RewardAdmin)

