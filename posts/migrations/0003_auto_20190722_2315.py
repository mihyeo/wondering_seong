# Generated by Django 2.0.13 on 2019-07-22 14:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190722_2242'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='liked_users', to=settings.AUTH_USER_MODEL, verbose_name='좋아요'),
        ),
    ]