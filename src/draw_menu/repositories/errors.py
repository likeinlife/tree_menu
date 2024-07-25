from dataclasses import dataclass

from settings.errors import BaseError


@dataclass(eq=False)
class MenuNotFoundError(BaseError):
    menu_slug: str

    @property
    def message(self) -> str:
        return f"Menu `{self.menu_slug}`not found"
