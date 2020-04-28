from django.db import models


def get_remote_image(url):
    result = urllib.urlretrieve(url)
    return File(open(result[0]))


# Create your models here.
class Formula(models.Model):
    imagelink = models.CharField(max_length=500)
    imagephoto = models.ImageField(upload_to='gamef1photos/')



    def __str__(self):
        return self.imagelink
