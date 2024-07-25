from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Menu(models.Model):
    name = models.CharField(_("menu_name"), max_length=100, unique=True)
    slug = models.CharField(_("slug"), max_length=250, blank=True, editable=False)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("parent_menu_item"),
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("menu_name")
        verbose_name_plural = _("menu_name_plural")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        parent_slug = ""
        if self.parent:
            obj = self.__class__.objects.filter(name=self.parent).first()
            parent_slug = f"{obj.slug}/" if obj else ""

        self.slug = f"{parent_slug}{slugify(self.name)}"
        super(Menu, self).save(*args, **kwargs)
