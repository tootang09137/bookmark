# Generated by Django 4.0.6 on 2022-07-28 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hashtag',
            new_name='r_hashtag',
        ),
    ]