# Generated by Django 3.0.8 on 2020-07-08 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
        migrations.RemoveField(
            model_name='news',
            name='url',
        ),
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
    ]
