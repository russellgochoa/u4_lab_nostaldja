from django.db import models

# Create your models here.


class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.TextField()

    def __str__(self):
        return self.name


class Fads(models.Model):
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='no name')
    description = models.CharField(max_length=100, default='no description')
    image_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
