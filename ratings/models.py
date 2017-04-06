from django.db import models
from django.utils import timezone

class User(models.Model):
    """User of ratings website."""

    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        s = "id=%s email=%s"

        return s % (self.id, self.email)


class Movie(models.Model):
    """Movie on ratings website."""

    title = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=10)
    tmdb_id = models.CharField(max_length=10)

    def __str__(self):
        s = "id=%s title=%s imdb_id=%s tmdb_id=%s"

        return  s % (self.id, self.title, self.imdb_id, self.tmdb_id)


class Ratings(models.Model):
    """Rating of a movie by a user."""

    movie_id = models.ForeignKey(Movie)
    user_id = models.ForeignKey(User)
    score = models.FloatField()

    def __str__(self):
        s = "id=%s movie_id=%s user_id=%s score=%s"

        return s % (self.id, self.movie_id, self.user_id, self.score)
