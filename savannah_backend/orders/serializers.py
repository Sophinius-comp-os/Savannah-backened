"""
SERIALIZERS Configuration for savannah/orders
"""

from rest_framework import serializers
from .models import Customer, Order
import re


class CustomerSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'code', 'phone']

    # Phone validation logic
    def validate_phone(self, value):
        phone_pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
        if not phone_pattern.match(value):
            raise serializers.ValidationError("Invalid phone number format. Use E.164 format.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        customer = CustomerSerializer(instance.customer)
        representation['customer'] = customer.data
        return representation
