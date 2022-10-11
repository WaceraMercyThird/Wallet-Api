
from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet, WalletViewSet, AccountViewSet, CardViewSet, TransactionViewSet, LoanViewSet, NotificationViewSet



router = routers.DefaltRouter()
routers.register("customer", CustomerViewSet)
routers.register("wallet", WalletViewSet)
routers.register("account", AccountViewSet)
routers.register("card", CardViewSet)
routers.register("transaction", TransactionViewSet)
routers.register("loan", LoanViewSet)
routers.register("notification", NotificationViewSet)








urlpatterns = [
    path("", include(router.urls)),
    ]