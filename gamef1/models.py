from django.db import models
from django.core.files import File
import urllib.request as urllib
import os

# from django.core.files import File
#
# import urllib.request as urllib

#
# def get_remote_image(url):
#     result = urllib.urlretrieve(url)
#     return File(open(result[0]))
#

# def test(url):
#     result = f"Teeeet {url}"
#     return result


def get_remote_image(url):
    result = urllib.urlretrieve(url)
    return File(open(result[0]))


# Create your models here.
class Formula(models.Model):
    imagelink = models.CharField(max_length=500)
    imagephoto = models.CharField(max_length=500)


    def save(self, *args, **kwargs):
        result = urllib.urlretrieve(self.imagelink)
        self.imagephoto = result[0]
        super(Formula, self).save(*args, **kwargs)



    def __str__(self):
        return self.imagelink
