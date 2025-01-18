# Generated by Django 5.1.3 on 2025-01-02 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание категории"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="название продукта"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание продукта"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="static/images",
                        verbose_name="изображение",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="цена за покупку")),
                ("created_at", models.DateTimeField(verbose_name="дата создания")),
                (
                    "updated_at",
                    models.DateTimeField(verbose_name="дата последнего изменения"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="catalog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "price", "created_at", "category"],
            },
        ),
    ]
