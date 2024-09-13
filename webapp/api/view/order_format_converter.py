from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from rest_framework.request import Request

from rest_framework import (
    viewsets,
    status
)
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from api.serializer.order_format_converter import CreateOrderFormatConverterSerializer


class OrderFormatConverterView(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        data_serializer = CreateOrderFormatConverterSerializer(data=request.data)
        if not data_serializer.is_valid():
            raise ValidationError("Incorrect json field")

        if self.contain_non_english(data_serializer["name"].value):
            raise ValidationError("Name contains Non-English characters")

        if self.not_capicalize(data_serializer["name"].value):
            raise ValidationError("Name is not capitalized")

        return Response(
            data={},
            status=status.HTTP_201_CREATED,
        )
    def contain_non_english(self, value: str) -> str:
        # only english and space is allowed

        # upper case is 65 ~ 90
        # lower case is 97 ~ 122
        # space is 32

        for c in value:
            ascii_value = ord(c)
            if not ((65 <= ascii_value <= 90) or (97 <= ascii_value <= 122) or ascii_value == 32):
                return True

        return False

    def not_capicalize(self, value: str):
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

        secperated_letter = value.split(' ')

        for letter in secperated_letter:
            origin_letter = letter[0]
            masked_letter = chr(ord(letter[0]) & ~(32))

            if origin_letter != masked_letter:
                return True

        return False


