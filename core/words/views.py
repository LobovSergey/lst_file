from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import WordsModel


class AnalyzedWordsListView(ListView):
    model = WordsModel
    template_name = "words_table.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        r = request.GET.get("key")
        return HttpResponse(f"{r}")

    def get_queryset(self) -> QuerySet[Any]:

        queryset = WordsModel.objects.get_queryset(secret_key="")

        return queryset
