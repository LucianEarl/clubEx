from django.db import models

class Excercise(models.Model):

    EXCERCISE_CHOICES = (
                        ("Yoga", "Yoga"),
                        ("Boxing","Boxing"),
                        ("Pilates","Pilates"),
                        ("Aerobics","Aerobics")
                    )
    excercise_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=EXCERCISE_CHOICES)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")
