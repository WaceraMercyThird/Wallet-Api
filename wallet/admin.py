from encodings import search_function
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    List_display = ("first_name", "last_name", "email")
    search_fields= ("first_name", "last_name")

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
