from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

__all__ = ['Genre', 'Singer', 'Track', 'Album']


# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Singer(models.Model):
    name = models.CharField(max_length=100)
    album = models.ManyToManyField('Album')

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    genres = models.ManyToManyField(Genre)
    singers = models.ManyToManyField(Singer)
    similar_movies = models.ManyToManyField("Track")
    album = models.ForeignKey("Album", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title


