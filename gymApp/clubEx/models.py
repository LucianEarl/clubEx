from django.db import models
from django.db.models.deletion import CASCADE


class CategoryManager(models.Manager):
    def create_category(self, category_name):
        category = self.create(category_name=category_name)
        category.save(using=self._db)
        return category


class Category(models.Model):
    category_name = models.CharField(max_length = 20)
    objects = CategoryManager()
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Category'
    def __str__(self):
        return self.category_name

