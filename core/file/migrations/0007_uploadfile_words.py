# Generated by Django 5.0.3 on 2024-03-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_uploadfile_secret_key'),
        ('words', '0003_remove_wordsmodel_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='words',
            field=models.ManyToManyField(to='words.wordsmodel'),
        ),
    ]
