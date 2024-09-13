from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from rest_framework.request import Request
    from rest_framework.response import Response

from rest_framework import (
    viewsets,
    status
)


class OrderFormatConverterView(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        pass
