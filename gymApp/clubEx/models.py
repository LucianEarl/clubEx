from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Exercise(models.Model):
    excercise_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, max_length=25, on_delete=CASCADE)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    objects = ExerciseManager()
    views = models.PositiveIntegerField(default=0)
    slug = models.AutoSlugField(populate_from="exercise_name") # helps view counter for video update
    likes = models.PositiveIntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    ) # relates to amount of likes video has been given

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.exercise_name + ': ' + self.category

    def __str__(self):
        return str(self.pk)
