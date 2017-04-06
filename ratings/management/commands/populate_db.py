from ratings.models import User, Movie, Ratings
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        ratings = CopyMapping(
            # model name
            Ratings,
            # path to movies.csv
            'ratings_sample.csv',
            # dict mapping model fields to csv headers
            dict(user_id='userId',movie_id='movieId',score='rating')
        )

        ratings.save()
