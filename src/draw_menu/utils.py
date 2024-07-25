from django.http import HttpRequest


def path_element(request: HttpRequest):
    return list(request.path.split("/"))
