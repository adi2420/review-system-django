# Generated by Django 3.1.5 on 2021-02-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_auto_20210210_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, upload_to='review/userreviews/images'),
        ),
    ]