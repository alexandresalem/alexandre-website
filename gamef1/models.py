from django.db import models


# Create your models here.
class Formula(models.Model):
    image = models.CharField(max_length=100)


    def __str__(self):
        return self.image
