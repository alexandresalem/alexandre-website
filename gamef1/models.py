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
    return (os.path.basename(url),File(open(result[0])))


# Create your models here.
class Formula(models.Model):
    imagelink = models.CharField(max_length=500)
    imagephoto = models.ImageField(upload_to='gamef1images')


    def save(self, *args, **kwargs):
        self.imagephoto = get_remote_image(self.imagelink)
        super(Formula, self).save(*args, **kwargs)
        # do custom stuff


    def __str__(self):
        return self.imagelink
