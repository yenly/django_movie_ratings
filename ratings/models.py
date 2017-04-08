from django.db import models
from django.utils import timezone

# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType

class User(models.Model):
    """User of ratings website."""

    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        s = "id=%s email=%s"

        return s % (self.id, self.email)


class Movie(models.Model):
    """Movie on ratings website."""

    movie_id = models.IntegerField(unique=True)
    movie_title = models.CharField(max_length=300,default='no title')
    imdb_id = models.CharField(max_length=15)
    tmdb_id = models.CharField(max_length=15)

    def __str__(self):
        s = "movie_id=%s title=%s imdb_id=%s tmdb_id=%s"

        return  s % (self.movie_id,  self.movie_title, self.imdb_id, self.tmdb_id)


class Ratings(models.Model):
    """Rating of a movie by a user."""

    movie_id = models.ForeignKey(Movie,to_field='movie_id')
    user_id = models.ForeignKey(User)
    score = models.FloatField()

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASACADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()

    def __str__(self):
        s = "id=%s movie_id=%s user_id=%s score=%s"

        return s % (self.id, self.movie_id, self.user_id, self.score)
