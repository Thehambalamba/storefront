from django.contrib.auth.models import User
from rest_framework import status
import pytest
from model_bakery import baker
from store.models import Collection, Product


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        api_client.force_authenticate(User(is_staff=is_staff))
    return do_authenticate


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED  # type: ignore

    def test_if_user_is_not_admin_returns_403(self, api_client, create_collection, authenticate):
        authenticate()

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN  # type: ignore

    def test_if_data_is_invalid_returns_403(self, api_client, create_collection, authenticate):
        authenticate(is_staff=True)

        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST  # type: ignore
        assert response.data['title'] is not None  # type: ignore

    def test_if_data_is_valid_returns_201(self, api_client, create_collection, authenticate):
        authenticate(is_staff=True)

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED  # type: ignore
        assert response.data['id'] > 0  # type: ignore


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        collection = baker.make(Collection)

        response = api_client.get(
            f'/store/collections/{collection.id}/')  # type: ignore

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,  # type: ignore
            'title': collection.title,
            'products_count': 0
        }

    def test_if_collection_doesnt_exists_returns_404(self, api_client):
        response = api_client.get('/store/collections/1/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_user_is_not_admin_collection_delete_returns_401(self, api_client):
        collection = baker.make(Collection)

        response = api_client.delete(
            f'/store/collections/{collection.id}/')  # type: ignore

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_admin_collection_delete_returns_204(self, api_client, authenticate):
        authenticate(is_staff=True)
        collection = baker.make(Collection)

        response = api_client.delete(
            f'/store/collections/{collection.id}/')  # type: ignore

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_collection_delete_returns_405(self, api_client, authenticate):
        authenticate(is_staff=True)
        collection = baker.make(Collection)

        baker.make(Product, collection=collection)
        response = api_client.delete(
            f'/store/collections/{collection.id}/')  # type: ignore

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
