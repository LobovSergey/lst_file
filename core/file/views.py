from typing import Any
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET

from file.functions import create_key
from .forms import UploadFileForm


@require_GET
def main(request):
    return render(request, "index.html")


class UploadFileFormView(FormView):
    form_class = UploadFileForm
    template_name = "upload_file.html"
    success_url = reverse_lazy("result")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = form.save()
            key = create_key(request)
            upload_file.slug = key
            upload_file.save()
            return redirect("result", key=key)
        return redirect("upload")
