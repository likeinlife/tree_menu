from django.contrib import admin
from django.db import models
from django.http import HttpRequest

from draw_menu.models import Menu
from draw_menu.utils import path_element


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0
    ordering = ("id",)

    def formfield_for_foreignkey(self, db_field: models.ForeignKey, request: HttpRequest, *_, **kwargs):
        if path_element(request)[-1] == "change":
            kwargs["queryset"] = Menu.objects.filter(parent=path_element(request)[-2])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    inlines = (MenuInline,)
