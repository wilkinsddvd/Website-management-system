# Generated by Django 4.2.16 on 2024-11-16 05:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0002_remove_author_authors_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='文章编号')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('readed_count', models.IntegerField(default=0, verbose_name='阅读次数')),
                ('admired_count', models.IntegerField(default=0, verbose_name='点赞次数')),
                ('liked_count', models.IntegerField(default=0, verbose_name='喜欢次数')),
                ('collected_count', models.IntegerField(default=0, verbose_name='收藏次数')),
                ('commented_count', models.IntegerField(default=0, verbose_name='评论次数')),
                ('up_time', models.DateTimeField(auto_now=True, verbose_name='上次修改时间')),
                ('status', models.CharField(choices=[('0', '正常'), ('1', '删除')], default='0', max_length=10, verbose_name='当前状态')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
            ],
            options={
                'ordering': ['-pub_time', 'id'],
            },
        ),
    ]
