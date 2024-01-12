from typing import Union

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Profile


def profiles_index(request: HttpRequest) -> Union[HttpResponse, Http404]:
    """
    Renders the 'profiles_index.html' template with
    a list of all profiles.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: A rendered HTML response containing
      the content of the 'profiles_index.html' template
      and a context variable 'profiles_list' with a list
      of all profiles.
    """
    try:
        profiles_list = Profile.objects.all()
    except Profile.DoesNotExist:
        raise Http404("No profile found")
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request: HttpRequest, username: str) -> Union[HttpResponse, Http404]:
    """
    Renders the 'profile.html' template for a specific user profile.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - username (str): The username of the profile to be displayed.

    Returns:
    - HttpResponse: A rendered HTML response containing the content of the 'profile.html' template
      and a context variable 'profile' with the details of the specified user profile.

    Raises:
    - Http404: If the specified user profile does not exist.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    context = {"profile": profile}
    return render(request, "profile.html", context)
