from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

class Exercise(models.Model):
    excercise_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, max_length=25, on_delete=CASCADE)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    objects = ExerciseManager()
    views = models.PositiveIntegerField(default=0)
    slug = models.AutoSlugField(populate_from="exercise_name")
    likes = models.PositiveIntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.exercise_name + ': ' + self.category



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

