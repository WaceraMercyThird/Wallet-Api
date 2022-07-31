from encodings import search_function
from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    List_display = ("first_name", "last_name", "email")
    search_fields= ("first_name", "last_name")

admin.site.register(Customer, CustomerAdmin)