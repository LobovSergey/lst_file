from typing import Any
from django import forms
from .models import UploadFile
from .decorator import word_analyzer
from .functions import create_key
from datetime import datetime


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ["file"]

    def clean_file(self):
        filename = self.cleaned_data["file"].name
        types = ["doc", "txt", "rtf"]
        if filename.split(".")[-1] not in types:
            raise forms.ValidationError(
                "Файл не является форматом 'doc', 'txt', 'rtf'")
        return self.cleaned_data["file"]

    @word_analyzer
    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)
