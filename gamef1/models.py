from django.db import models
from django.core.files import File

import urllib.request as urllib


def get_remote_image(url):
    result = urllib.urlretrieve(url)
    return File(open(result[0]))


# Create your models here.
class Formula(models.Model):
    imagelink = models.CharField(max_length=100)
    imagephoto = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        # self.imagephoto = get_remote_image(self.imagelink)
        self.imagephoto = 'Testando'
        super(Formula, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.imagelink
