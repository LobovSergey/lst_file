# Generated by Django 5.0.3 on 2024-03-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_uploadfile_delete_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='text/'),
        ),
    ]