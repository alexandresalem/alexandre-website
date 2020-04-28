from django.db import models


# Create your models here.
class Formula(models.Model):
    imagelink = models.CharField(max_length=500)
    imagephoto = models.ImageField(upload_to='gamef2/')



    def __str__(self):
        return self.imagelink
