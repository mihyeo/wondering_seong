# Generated by Django 2.0.13 on 2019-08-08 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190808_0119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': '게시글 좋아요', 'verbose_name_plural': '게시글 좋아요'},
        ),
    ]
