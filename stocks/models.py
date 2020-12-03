from django.db import models


class Company(models.Model):
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    market = models.CharField(max_length=50)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    date = models.DateField()
    headline = models.CharField(max_length=300)
    story = models.TextField()
    sentiment = models.CharField(max_length=100, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.headline}'
