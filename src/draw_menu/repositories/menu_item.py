from draw_menu.models import Menu
from draw_menu.repositories.errors import MenuNotFoundError


class MenuRepository:
    def fetch_menu(self, menu_slug: str) -> Menu:
        """Fetch menu object, including children."""
        result = Menu.objects.filter(slug=menu_slug).prefetch_related("children").first()
        if not result:
            raise MenuNotFoundError(menu_slug=menu_slug)
        return result
