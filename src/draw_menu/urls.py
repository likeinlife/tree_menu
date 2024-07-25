from django.urls import path

from draw_menu.views import home

urlpatterns = [
    path("", home, name="home"),
    path("<path:path>", home, name="home"),
]
