import os

from django.core.files.storage import FileSystemStorage
from django.db import models

from gettingstarted.settings import BASE_DIR


class F1Prediction(models.Model):
    image = models.ImageField(upload_to='gamef1')
    chassis = models.CharField(max_length=50, blank=True)
    constructor = models.CharField(max_length=50, blank=True)
    season = models.CharField(max_length=4, blank=True)
    probability = models.FloatField(blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.image.name

    @property
    def get_absolute_image_url(self):
        return os.path.join(BASE_DIR, self.image.name)

    @property
    def get_absolute_image_full_url(self):
        storage = FileSystemStorage()
        return storage.path(self.get_absolute_image_url)


class Chassis(models.Model):
    chassis = models.CharField(max_length=50)
    constructor = models.CharField(max_length=50, blank=True)
    chassis_fullname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.constructor} - {self.chassis}'


