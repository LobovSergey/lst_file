# Generated by Django 5.0.3 on 2024-03-26 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0008_remove_uploadfile_words'),
        ('words', '0003_remove_wordsmodel_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordsmodel',
            name='document',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='file.uploadfile'),
        ),
    ]
