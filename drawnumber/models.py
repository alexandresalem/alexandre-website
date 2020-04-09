from django.db import models


# Create your models here.
class Number(models.Model):
    drawing = models.CharField(max_length=1000)
    drawingcode = models.TextField(max_length=20000, default='2')

    def __str__(self):
        return self.drawing
