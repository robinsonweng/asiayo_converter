from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    pass


from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.enums import CurrencyType


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=255)
    district = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)


class CreateOrderFormatConverterSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    address = AddressSerializer()
    price = serializers.IntegerField()
    currency = serializers.CharField(max_length=255)
