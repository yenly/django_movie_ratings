from ratings.models import Movie
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        movies = CopyMapping(
            # model name
            Movie,
            # path to movies.csv
            'data/movies.csv',
            # dict mapping model title to csv header
            dict(title='title'),
            static_mapping = {
                'imdb_id': '',
                'tmdb_id': ''
            }
        )

        movies.save()
