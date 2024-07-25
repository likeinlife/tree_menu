from django.http import HttpRequest
from django.shortcuts import render

from draw_menu.container import get_container
from draw_menu.repositories.menu_item import MenuRepository


def home(request: HttpRequest, *_, **__):
    return render(request, "index.html")


def htmx_submenu(request: HttpRequest, slug: str):
    menu_repository = get_container().get(MenuRepository)
    context = {"submenu": menu_repository.fetch_menu(slug)}
    return render(
        request,
        "htmx/submenu.html",
        context,
    )
