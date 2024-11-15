# Create your models here.
from django.db import models


class CarouselItem(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')
    link = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='countries/')  # Path where images are stored
    flag_image = models.ImageField(upload_to='flags/')  # Path for flag images
    url = models.URLField(max_length=200, blank=True, null=True)  # Optional link

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class UniversityLogo(models.Model):
    name = models.CharField(max_length=100)
    logo_image = models.ImageField(upload_to='university_logos/')  # Adjust path as needed

    def __str__(self):
        return self.name
