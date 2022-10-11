from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from wallet import Customer


class CustomerSerializer(serializers.modelSerializer):

    class meta:
        model = Customer
        field = (" first_name", " email", "age")