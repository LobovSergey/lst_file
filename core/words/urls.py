from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import AnalyzedWordsListView

urlpatterns = [path("<str:key>", AnalyzedWordsListView.as_view(), name="result")]
