from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        "Category",
        related_name="children",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=200)
