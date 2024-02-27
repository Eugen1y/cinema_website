from django.db import models

from django.db import models


class Director(models.Model):
    """ Model representing a movie director."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the director."""
        return self.name


class Actor(models.Model):
    """ Model representing a movie actor."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the actor."""
        return self.name


class Movie(models.Model):
    """Model representing a movie."""

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        """Custom save method to generate a unique slug based on the movie title and year."""

        self.slug = f"{self.title.replace(' ', '_')}_{self.year}"
        super().save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the movie."""
        return self.title
