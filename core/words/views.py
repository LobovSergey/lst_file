from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import Http404
from django.views.generic import DetailView, ListView
from file.models import UploadFile
from .models import WordsModel


class AnalyzedWordsListView(ListView):
    template_name = "words_table.html"
    slug_url_kwarg = "key"
    paginate_by = 10
    context_object_name = "objects"

    def get_queryset(self) -> QuerySet[Any]:
        global key
        global counter
        key = self.kwargs.get(self.slug_url_kwarg, None)
        object = UploadFile.objects.get(slug=key)
        counter = object.counter_words
        queryset = object.words.all().order_by("-term_frequency")
        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["key"] = key
        data["counter"] = counter
        return data
