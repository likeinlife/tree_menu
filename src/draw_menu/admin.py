from django.contrib import admin

from draw_menu.models import Menu


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0
    ordering = ("id",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    inlines = (MenuInline,)
