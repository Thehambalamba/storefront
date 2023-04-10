from rest_framework import status
from rest_framework.test import APIClient
import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED  # type: ignore

    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN  # type: ignore

    def test_if_data_is_invalid_returns_403(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST  # type: ignore
        assert response.data['title'] is not None  # type: ignore

    def test_if_data_is_valid_returns_201(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED  # type: ignore
        assert response.data['id'] > 0  # type: ignore
