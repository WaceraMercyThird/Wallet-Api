from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from wallet.models import Customer,Wallet, Account, Loan, Card, Notification, Transaction



class CustomerSerializer(serializers.modelSerializer):

    class meta:
        model = Customer
        field = (" first_name", " email", "age")


class WalletSerializer(serializers.modelSerializer):

    class meta:
        model = Wallet
        field = (" first_name", " email", "age")


class AccountSerializer(serializers.modelSerializer):

    class meta:
        model = Account
        field = (" first_name", " email", "age")

class CardSerializer(serializers.modelSerializer):

    class meta:
        model = Card
        field = (" first_name", " email", "age")


class TransactionSerializer(serializers.modelSerializer):

    class meta:
        model = Transaction
        field = (" first_name", " email", "age")


class LoanSerializer(serializers.modelSerializer):

    class meta:
        model = Loan
        field = (" first_name", " email", "age")


class NotificationSerializer(serializers.modelSerializer):

    class meta:
        model = Notification
        field = (" first_name", " email", "age")