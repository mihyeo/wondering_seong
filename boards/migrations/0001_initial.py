# Generated by Django 2.0.13 on 2019-07-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성된 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 시간')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('view_count', models.IntegerField(default=0, verbose_name='조회수')),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성된 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 시간')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
            ],
            options={
                'verbose_name': '질의응답',
                'verbose_name_plural': '질의응답',
            },
        ),
    ]