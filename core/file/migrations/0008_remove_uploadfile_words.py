# Generated by Django 5.0.3 on 2024-03-26 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0007_uploadfile_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='words',
        ),
    ]