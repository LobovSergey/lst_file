from typing import Any
from django import forms
from .models import UploadFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = "__all__"

    def clean_file(self):
        filename = self.cleaned_data["file"].name
        types = ["doc", "txt", "rtf"]
        print(filename)
        if filename.split(".")[-1] not in types:
            raise forms.ValidationError("Файл не является форматом 'doc', 'txt', 'rtf'")
        return self.cleaned_data["file"]