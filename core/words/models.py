from django.db import models
from file.models import UploadFile


class WordsModel(models.Model):
    word = models.CharField(max_length=50, editable=False)
    counter = models.PositiveIntegerField()
    term_frequency = models.FloatField()
    document = models.ForeignKey(
        UploadFile,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        related_name="words",
    )
