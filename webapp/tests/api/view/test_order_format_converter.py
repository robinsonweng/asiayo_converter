from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    pass


from rest_framework.test import (
    APITestCase
)


class APITestBase(APITestCase):
    maxDiff = None


class TestOrderFormatConverterView(APITestBase):
    def test_make_this_test_pass(self):
        assert False
