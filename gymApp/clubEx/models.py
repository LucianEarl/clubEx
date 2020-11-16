from django.db import models

class Exercise(models.Model):

    EXERCISE_CHOICES = (
                        ("Yoga", "Yoga"),
                        ("Boxing","Boxing"),
                        ("Pilates","Pilates"),
                        ("Aerobics","Aerobics")
                    )
    excercise_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=EXERCISE_CHOICES)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.pet_name + ': ' + str(self.imagefile) + self.colour + ' ' + self.species
