from django.urls import path
from .views import register_account, register_card, register_customer, register_loan, register_notification, register_reward, register_thirdParty, register_wallet, register_transaction

urlpatterns = [
    path("register/", register_customer, name="regisration"),
    path("signup/", register_wallet, name="register_signup"),
    path("accounts/", register_account, name="register_accounts"),
    path("transactions/", register_transaction, name="register_transactions"),
    path("cards/", register_card, name="register_cards"),
    path("thirdPartys/", register_thirdParty, name="register_thirdPartys"),
    path("notifications/", register_notification, name="register_notifications"),
    path("loans/", register_loan, name="register_loans"),
    path("rewards/", register_reward, name="register_rewards")






]
