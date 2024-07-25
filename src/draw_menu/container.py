from functools import lru_cache

from dishka import Container, Provider, Scope, make_container, provide

from draw_menu.repositories import MenuRepository


class AppProvider(Provider):
    scope = Scope.APP

    @provide
    def _menu_item(self) -> MenuRepository:
        return MenuRepository()


@lru_cache(1)
def get_container() -> Container:
    return make_container(AppProvider())
