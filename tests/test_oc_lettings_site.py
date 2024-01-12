from conftest import client
from django.urls import resolve, reverse


def test_oc_lettings_site_index():
    url = reverse("index")
    response = client.get(url)
    content = response.content.decode()

    assert response.status_code == 200
    assert resolve(url).view_name == "index"
    assert '<h1 class="page-header' in content
