# Generated by Django 3.1.5 on 2021-02-08 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20210209_0352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='editing_expires_on_date',
            new_name='expire',
        ),
    ]