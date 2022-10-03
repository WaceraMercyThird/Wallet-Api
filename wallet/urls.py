from django.urls import path
from .views import list_customers, register_account, register_card, register_customer, register_loan, register_notification, register_reward, register_thirdParty, register_wallet, register_transaction, customer_profile, edit_customer, list_wallets, list_accounts,list_transactions,list_cards,list_loans,list_rewards,list_thirdPartys,list_notifications, wallet_profile,account_profile,transaction_profile, card_profile,thirdParty_profile, notification_profile, loan_profile, reward_profile,edit_account,edit_card,edit_loan,edit_notification,edit_reward,edit_thirdParty,edit_transaction,edit_wallet

urlpatterns = [
    path("register/", register_customer, name="regisration"),
    path("signup/", register_wallet, name="register_signup"),
    path("accounts/", register_account, name="register_accounts"),
    path("transactions/", register_transaction, name="register_transactions"),
    path("cards/", register_card, name="register_cards"),
    path("thirdPartys/", register_thirdParty, name="register_thirdPartys"),
    path("notifications/", register_notification, name="register_notifications"),
    path("loans/", register_loan, name="register_loans"),
    path("rewards/", register_reward, name="register_rewards"),
    # path("receipts/", register_receipt, name="register_receipts"),

    path("list/", list_customers, name="list_customers"),
    path("list/", list_wallets, name="list_wallets"),
    path("list/", list_accounts, name="list_accounts"),
    path("list/", list_transactions, name="list_transactions"),
    path("list/", list_cards, name="list_cards"),
    path("list/", list_thirdPartys, name="list_thirdPartys"),
    path("list/", list_notifications, name="list_notifications"),
    path("list/", list_loans, name="list_laons"),
    path("list/", list_rewards, name="list_rewards"),
    # path("list/", list_receipts, name="list_receipts"),
    

    path("customers/<int:id>/", customer_profile, name="customer_profile"),
    path("wallets/<int:id>/", wallet_profile, name="wallet_profile"),
    path("accounts/<int:id>/", account_profile, name="account_profile"),
    path("transactions/<int:id>/", transaction_profile, name="transaction_profile"),
    path("cards/<int:id>/", card_profile, name="card_profile"),
    path("thirdPartys/<int:id>/", thirdParty_profile, name="thirdParty_profile"),
    path("notifications/<int:id>/", notification_profile, name="notification_profile"),
    path("loans/<int:id>/", loan_profile, name="loan_profile"),
    path("rewards/<int:id>/", reward_profile, name="reward_profile"),
    


    path("customers/edit/<int:id>/", edit_customer, name="edit_customer"),
    path("wallets/edit/<int:id>/", edit_wallet, name="edit_wallet"),
    path("accounts/edit/<int:id>/", edit_account, name="edit_account"),
    path("transactions/edit/<int:id>/", edit_transaction, name="edit_transaction"),
    path("cards/edit/<int:id>/", edit_card, name="edit_card"),
    path("thirdPartys/edit/<int:id>/", edit_thirdParty, name="edit_thirdParty"),
    path("notifications/edit/<int:id>/", edit_notification, name="edit_notification"),
    path("loans/edit/<int:id>/", edit_loan, name="edit_loan"),
    path("rewards/edit/<int:id>/", edit_reward, name="edit_reward"),
   

]
