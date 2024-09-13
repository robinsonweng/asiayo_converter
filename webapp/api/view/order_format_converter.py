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

        return Response(
            data={},
            status=status.HTTP_201_CREATED,
        )
