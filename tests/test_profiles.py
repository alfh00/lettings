import pytest
from conftest import client
from django.contrib.auth.models import User
from django.urls import resolve, reverse

from profiles.models import Profile

# path('', views.profiles_index, name='profiles_index'),
# path('<str:username>/', views.profile, name='profile'),


@pytest.mark.django_db
def test_profiles_index():
    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert resolve(url).view_name == "profiles_index"


@pytest.mark.django_db
def test_profile_view():
    user = User.objects.create(username="test_user", password="test_password")

    profile = Profile.objects.create(user=user, favorite_city="test city")

    url = reverse("profile", args=[user.username])
    response = client.get(url)
    content = response.content.decode()

    assert response.status_code == 200
    assert profile.user.username in content
    assert profile.favorite_city in content
    assert resolve(url).view_name == "profile"
