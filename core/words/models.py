from django.db import models


class WordsModel(models.Model):
    word = models.CharField(max_length=50, editable=False)
    counter = models.PositiveIntegerField()
    term_frequency = models.FloatField()
    secret_key = models.CharField(max_length=50)
