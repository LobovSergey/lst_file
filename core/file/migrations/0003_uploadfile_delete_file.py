# Generated by Django 5.0.3 on 2024-03-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_file_title_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='text/')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
