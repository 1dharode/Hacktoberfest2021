# Generated by Django 4.0 on 2022-06-15 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_likepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='no_of_lokes',
            new_name='no_of_likes',
        ),
    ]
