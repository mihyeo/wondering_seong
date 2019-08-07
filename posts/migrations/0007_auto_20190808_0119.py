# Generated by Django 2.0.13 on 2019-08-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190807_0200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': '댓글', 'verbose_name_plural': '댓글'},
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'basic'), (1, 'before_sex'), (2, 'sex_ing'), (3, 'after_sex'), (4, 'news')], verbose_name='카테고리'),
        ),
    ]
