from django.db import models


# Create your models here.
class Formula(models.Model):
    f1image = models.ImageField(upload_to='gamef1/')
    f1text = models.CharField(max_length=500)



    def __str__(self):
        return self.f1image
