# Generated by Django 5.0.7 on 2024-07-24 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="menu_name")),
                ("slug", models.CharField(blank=True, editable=False, max_length=250, verbose_name="slug")),
                ("url", models.CharField(max_length=250, verbose_name="url")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="draw_menu.menu",
                        verbose_name="parent_menu_item",
                    ),
                ),
            ],
            options={
                "verbose_name": "menu_name",
                "verbose_name_plural": "menu_name_plural",
            },
        ),
    ]
