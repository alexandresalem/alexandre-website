from django.db import models
from django.core.files.storage import FileSystemStorage

fsgamef1 = FileSystemStorage(location='/media/gamef1')
# Create your models here.
class Formula(models.Model):
    imagelink = models.CharField(max_length=100)
    imagephoto = models.ImageField(storage=fsgamef1, default='Noimage')
    def __str__(self):
        return self.imagelink
