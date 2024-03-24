from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import AnalyzedWords


class AnalyzedWordsListView(ListView):
    model = AnalyzedWords
    template_name = ""

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset().filter()
        return queryset
