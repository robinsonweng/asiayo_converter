from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    List,
)

if TYPE_CHECKING:
    from rest_framework.request import Request

from rest_framework import (
    viewsets,
    status
)
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema

from api.serializer.order_format_converter import (
    CreateOrderFormatConverterSerializer
)
from api.enums import SupportedCurrency


class OrderFormatConverterView(viewsets.ViewSet):
    @swagger_auto_schema(
        request_body=CreateOrderFormatConverterSerializer,
        responses={
            status.HTTP_400_BAD_REQUEST: None,
            status.HTTP_201_CREATED: CreateOrderFormatConverterSerializer,
        }
    )
    def create(self, request: Request) -> Response:
        data_serializer = CreateOrderFormatConverterSerializer(
            data=request.data
        )
        if not data_serializer.is_valid():
            raise ValidationError("Incorrect json field")

        name = data_serializer["name"].value
        price = data_serializer["price"].value
        currency = data_serializer["currency"].value

        if currency not in SupportedCurrency:
            raise ValidationError("Currency format is wrong")
        currency = SupportedCurrency(currency)

        order_name = OrderName(name)
        order_fee = OrderFee(price, currency)

        if order_name.contain_non_english():
            raise ValidationError("Name contains Non-English characters")

        if order_name.not_capicalize():
            raise ValidationError("Name is not capitalized")

        if order_fee.price_over_2000():
            raise ValidationError("Price is over 2000")

        price, currency = order_fee.convert_USD_to_TWD()
        data_serializer.validated_data["price"] = price
        data_serializer.validated_data["currency"] = currency

        return Response(
            data=data_serializer.validated_data,
            status=status.HTTP_201_CREATED,
        )


class OrderName(object):
    def __init__(self, name) -> None:
        self.name = name

    def contain_non_english(self) -> bool:
        # only english and space is allowed

        # upper case is 65 ~ 90
        # lower case is 97 ~ 122
        # space is 32

        for c in self.name:
            ascii_value = ord(c)
            if not (
                (65 <= ascii_value <= 90) or
                (97 <= ascii_value <= 122) or
                ascii_value == 32
            ):
                return True

        return False

    def not_capicalize(self) -> bool:
        """
            this function assume that the value already check by
            contain_non_english function

            the c & ~(32) is a way to force ascii char into upper
            case using bitwise operation, e.g.

            ascii_a = ord('a') # 97

            97 & ~(32)

            97     = 01100001
            ~(32)  = 11011111
            ------- and ---------
            65     = 01000001

            ascii_a = ord('A') # 65

            65 & ~(32)

            65     = 01000001
            ~(32)  = 11011111
            ------- and ---------
            65     = 01000001

        """

        secperated_letter = self.name.split(' ')

        for letter in secperated_letter:
            origin_letter = letter[0]
            masked_letter = chr(ord(letter[0]) & ~(32))

            if origin_letter != masked_letter:
                return True

        return False


class OrderFee(object):
    def __init__(self, price: int, currency: SupportedCurrency) -> None:
        self.price = price
        self.currency = currency

    def price_over_2000(self) -> bool:
        if self.price > 2000:
            return True
        return False

    def convert_USD_to_TWD(self):
        if self.currency == SupportedCurrency.USD:
            price = self.price * 31
            currency = SupportedCurrency.TWD.value
            return price, currency

        return self.price, self.currency
