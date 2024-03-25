from typing import Any
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from .forms import UploadFileForm


@require_GET
def main(request):
    return render(request, "index.html")


class UploadFileFormView(FormView):
    form_class = UploadFileForm
    template_name = "upload_file.html"
    success_url = reverse_lazy("result")

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)
