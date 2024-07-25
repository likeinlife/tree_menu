from django.urls import path

from draw_menu.views import home, htmx_submenu

urlpatterns = [
    path("", home, name="home"),
    path("htmx/submenu/<path:slug>", htmx_submenu, name="htmx_submenu"),
]
