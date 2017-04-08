from ratings.models import Movie
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open('data/links.csv') as links:
            links = csv.DictReader(links)
            for row in links:
                movieID = row['movieId']
                new_movie = Movie.objects.filter(movie_id=movieID).update(imdb_id=row['imdbId'],tmdb_id=row['tmdbId'])
