# Generated by Django 4.2.11 on 2024-04-07 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finalapp', '0004_dccomics_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='author',
            field=models.ForeignKey(default='12', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]