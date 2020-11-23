from django.db import models
from account.models import Account
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator


class CategoryManager(models.Manager):
    def create_category(self, category_name):
        category = self.create(category_name=category_name)
        category.save(using=self._db)
        return category

class ExerciseManager(models.Manager):
    def create_exercise(self, exercise_name, category, videofile, length):
        exercise = self.create(
            exercise_name=exercise_name,
            category=category,
            videofile=videofile,
            length=length
        )
        exercise.save(using=self._db)
        return exercise

class UserVidWatchManager(models.Manager):
    def create_watchedVid(self, joined_user, joined_video, specific_views):
        watchedVid = self.create(
            joined_user=joined_user,
            joined_video=joined_video,
            specific_views=specific_views,
        )
        watchedVid.save(using=self._db)
        return watchedVid

class Category(models.Model):
    category_name = models.CharField(max_length = 20)
    objects = CategoryManager()
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category_name

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, max_length=25, on_delete=CASCADE)
    videofile= models.FileField(upload_to='videos/', verbose_name="")
    views = models.PositiveIntegerField(default=0)
    length = models.CharField(max_length=12, blank=True)
    likes = models.PositiveIntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    ) # relates to amount of likes video has been given
    objects = ExerciseManager()

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.exercise_name + ': ' + str(self.videofile)

    def __str__(self):
        return str(self.pk)

class UserVidWatch(models.Model):
    joined_user = models.ForeignKey(Account, on_delete=CASCADE)
    joined_video = models.ForeignKey(Exercise, on_delete=CASCADE)
    specific_views = models.PositiveIntegerField(default=0)
    objects = UserVidWatchManager()

    def __str__(self):
        return self.joined_user + " " + self.joined_video
