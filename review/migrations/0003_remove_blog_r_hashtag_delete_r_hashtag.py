# Generated by Django 4.0.6 on 2022-07-28 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_hashtag_r_hashtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='r_hashtag',
        ),
        migrations.DeleteModel(
            name='r_hashtag',
        ),
    ]