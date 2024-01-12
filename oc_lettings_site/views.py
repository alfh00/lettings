from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Renders the 'index.html' template.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: A rendered HTML response containing the content of the 'index.html' template.
    """
    return render(request, "index.html")
