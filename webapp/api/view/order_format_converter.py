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
                return  True

        return False
