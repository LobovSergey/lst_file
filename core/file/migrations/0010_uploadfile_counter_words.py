# Generated by Django 5.0.3 on 2024-03-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0009_rename_secret_key_uploadfile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='counter_words',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]