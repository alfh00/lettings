from django.shortcuts import render


class CustomErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # handling specific error codes and render custom views
        if response.status_code == 404:
            return render(request, "404.html", status=404)
        elif response.status_code == 500:
            return render(request, "500.html", status=500)

        return response
