from django.template import RequestContext
from django.templatetags.cache import register

from draw_menu.container import get_container
from draw_menu.repositories.menu_item import MenuRepository


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context: RequestContext, menu_slug: str) -> dict:
    slug = context.request.path.strip("/")
    menu_repository = get_container().get(MenuRepository)

    menu = menu_repository.fetch_menu(slug if slug else menu_slug)

    return {"menu": menu}
