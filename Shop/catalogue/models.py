from django.db import models
from category.models import Category
from tag.models import Tag

# class Category(models.Model):
#     name = models.CharField(max_length = 28)
# class Tag(models.Model):
#     name = models.CharField(max_length=28)
class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length = 50)
    stock = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    image_url = models.URLField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name



