# Generated by Django 4.2.11 on 2024-04-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0005_monster_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='dccomics',
            name='url',
            field=models.URLField(default='hi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monster',
            name='url',
            field=models.URLField(default='hi'),
            preserve_default=False,
        ),
    ]