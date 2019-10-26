from django.db import models
from django.contrib.auth import get_user_model

GENRES = [
    ('cy', 'Comedy'),
    ('de', 'Action'),
    ('ae', 'Adventure'),
    ('ce', 'Crime'),
    ('da', 'Drama'),
    ('fy', 'Fantasy'),
    ('hl', 'Historical'),
    ('hr', 'Horror')
]

ROLES = [
    ('ar', 'Actor'),
    ('pr', 'Producer'),
]

class Man(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_born = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_men'
    )

    def __str__(self):
        return self.first_name



class Film(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date_of_production = models.DateField()
    genre = models.CharField(max_length=2, choices=GENRES)
    actor = models.ForeignKey(
        Man,
        null=True,
        on_delete=models.SET_NULL,
        related_name="played_films"
    )
    producer = models.ForeignKey(
        Man,
        null=True,
        on_delete=models.SET_NULL,
        related_name="produced_films"
    )
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_films'
    )

    def __str__(self):
        return self.title
