from django.http import HttpResponse
import uuid

class IDCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        idcookie = request.COOKIES.get('idcookie')
        if not idcookie:
            idcookie = str(uuid.uuid4())
        request.idcookie = idcookie  # Set the idcookie as an attribute of the request

        response = self.get_response(request)

        response.set_cookie('idcookie', idcookie)  # Set the idcookie in the response's cookies

        return response