from __future__ import annotations
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    pass


from rest_framework import (
    status
)
from rest_framework.test import (
    APITestCase
)
from rest_framework.reverse import reverse


class APITestBase(APITestCase):
    maxDiff = None


class TestOrderFormatConverterView(APITestBase):
    view_name = "api:orders-list"

    def test_given_incorrect_field_key_should_400(self):

        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2050",
            "currncy": "TWD"
        }
        url = reverse(self.view_name)
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        expected_response = ["Incorrect json field"]
        self.assertEqual(response.json(), expected_response)

    def test_given_non_english_character_name_should_400(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn!",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2050",
            "currency": "TWD"
        }
        url = reverse(self.view_name)
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        expected_response = ["Name contains Non-English characters"]
        self.assertEqual(response.json(), expected_response)

    def test_make_this_test_pass(self):

        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2050",
            "currency": "TWD"
        }

        url = reverse(self.view_name)
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_response = {}
        self.assertDictEqual(response.json(), expected_response)

