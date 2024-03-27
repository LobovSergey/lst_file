from typing import Any
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET
from file.functions import create_key, get_counter
from .forms import UploadFileForm


@require_GET
def main(request):
    return redirect("upload")


class UploadFileFormView(FormView):
    form_class = UploadFileForm
    template_name = "upload_file.html"
    success_url = reverse_lazy("result")

    def get_context_data(self, error="", **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["error"] = error
        return data

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if (not request.FILES and not request.POST["secret_key"]) or (request.FILES and request.POST["secret_key"]):
            error_message = "Нужно выбрать 1 вариант"
            return render(request=request,  template_name="upload_file.html", context=self.get_context_data(error=error_message))
        elif request.FILES and not request.POST["secret_key"]:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                upload_file = form.save()
                key = create_key(request)
                counter = get_counter()
                upload_file.slug = key
                upload_file.counter_words = counter
                upload_file.save()
                return redirect("result", key=key)
            return render(request=request,  template_name="upload_file.html", context=self.get_context_data())
        else:
            return redirect("result", key=request.POST["secret_key"])
