from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import WordsModel


class AnalyzedWordsListView(ListView):
    model = WordsModel
    template_name = "words_table.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = WordsModel.objects.filter(secret_key=1)
        return super().get_queryset()
