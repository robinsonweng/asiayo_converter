from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass


from rest_framework.routers import SimpleRouter
from api.view.order_format_converter import OrderFormatConverterView


order_router = SimpleRouter(
    trailing_slash=False,
)
order_router.register(
    r"orders",
    OrderFormatConverterView,
    basename="orders",
)

v1_router = SimpleRouter(
    trailing_slash=False,
)

v1_router.registry.extend(order_router.registry)
