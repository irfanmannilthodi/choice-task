# Generated by Django 4.2.11 on 2024-04-08 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0007_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='author',
        ),
    ]