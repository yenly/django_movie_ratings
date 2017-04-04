# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('released_at', models.DateTimeField()),
                ('imdb_id', models.CharField(max_length=10)),
                ('tmdb_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratings.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('zipcode', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='ratings',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratings.User'),
        ),
    ]
