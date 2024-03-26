from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import WordsModel
from file.models import UploadFile


class AnalyzedWordsListView(DetailView):
    model = UploadFile
    template_name = "words_table.html"
    slug_url_kwarg = "key"
