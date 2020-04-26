from django.db import models
from django.core.files import File
import os
import urllib.request as urllib


# Create your models here.
class Formula(models.Model):
    imagelink = models.URLField(max_length=100)
    imagephoto = models.ImageField(upload_to='images')
    def save(self, *args, **kwargs):
        if self.imagelink and not self.imagephoto:
            result = urllib.urlretrieve(self.imagelink)
            self.imagephoto.save(os.path.basename(self.imagelink), File(open(result[0])))
            self.save()
            super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.imagelink

def get_remote_image(self):
