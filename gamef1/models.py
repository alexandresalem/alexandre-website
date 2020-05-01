from django.db import models
from django import forms

# Create your models here.
class Formula(models.Model):
    f1image = models.ImageField(upload_to='gamef1/')



class Answer(models.Model):
    GUESSES = (
        ('1st', "First"),
        ('2nd', 'Second'),
        ('3rd','Third')
    )


    guess = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=100, blank=True)
    chassis = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.guess
