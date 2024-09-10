from django.db import models
from treebeard.mp_tree import MP_Node
from catalog.managers import CategoryQuerySet

# Create your models here.


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    objects = CategoryQuerySet.as_manager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class OptionGroup(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Option Group"
        verbose_name_plural = "Option Groups"


class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Option Group Value"
        verbose_name_plural = "Option Group Values"


class ProductClass(models.Model):
    title = models.CharField(max_length=256, db_index=True)
    descriptor = models.CharField(max_length=2048, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    track_stock = models.BooleanField(default=True)
    require_shop = models.BooleanField(default=True)
    options = models.ForeignKey("OptionGroup", blank=True)

    def __str__(self) -> str:
        return self.title

    @property
    def has_attribute(self):
        return self.attribute.exists()

    class Meta:
        verbose_name = "Product Class"
        verbose_name_plural = "Product Classes"
