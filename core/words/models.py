from django.db import models
from ..file.models import UploadFile


class AnalyzedWords(models.Model):
    word = models.CharField(max_length=50, required=True, editable=False)
    counter = models.PositiveIntegerField()
    term_frequency = models.FloatField()
    document = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
