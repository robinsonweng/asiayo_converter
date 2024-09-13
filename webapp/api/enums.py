from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    pass

from enum import (
    Enum,
    EnumMeta,
)


class EnumContains(EnumMeta):
    def __contains__(self: type, member: object) -> bool:
        try:
            self(member)
        except ValueError:
            return False
        else:
            return True


class SupportedCurrency(str, Enum, metaclass=EnumContains):
    TWD = "TWD"
    USD = "USD"
