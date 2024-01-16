import pytest
from conftest import client
from django.urls import resolve, reverse

from lettings.models import Address, Letting

# path('', views.lettings_index, name='lettings_index'),
# path('<int:letting_id>/', views.letting, name='letting'),


@pytest.mark.django_db
def test_lettings_index():
    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert resolve(url).view_name == "lettings_index"


@pytest.mark.django_db
def test_letting_view():
    address = Address.objects.create(
        number=1111, street="Street test", city="City test", state="State test", zip_code="1111", country_iso_code="FR"
    )
    print(address)
    letting = Letting.objects.create(title="title test", address=address)

    url = reverse("letting", args=[letting.id])
    response = client.get(url)
    content = response.content.decode()

    assert response.status_code == 200
    assert letting.title in content
    assert letting.address.zip_code in content
    assert resolve(url).view_name == "letting"
