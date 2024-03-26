from django.db import models


class UploadFile(models.Model):
    file = models.FileField(upload_to="text/")
    slug = models.CharField(
        max_length=100, editable=True, default=None, null=True)
