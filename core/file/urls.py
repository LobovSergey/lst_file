from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import UploadFileFormView

urlpatterns = [path("create/", UploadFileFormView.as_view())]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
