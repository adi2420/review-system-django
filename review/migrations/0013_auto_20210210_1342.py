# Generated by Django 3.1.5 on 2021-02-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_auto_20210210_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertprofile',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]