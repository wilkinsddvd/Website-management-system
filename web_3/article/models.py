from uuid import uuid4
from django.db import models
from django.urls import reverse

class Article(models.Model):
    # 11.16 更新根据get_absolute_url()方法修改url
    def get_absolute_url(self):
        return reverse('article:article_detail',kwargs={'article_id':self.id})
    # 文章类型
    ARTICLE_STATUS = (
        ('0', '正常'),
        ('1', '删除'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, auto_created=True,verbose_name='文章编号')
    title = models.CharField(max_length=200, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    readed_count = models.IntegerField(default=0, verbose_name='阅读次数')
    admired_count = models.IntegerField(default=0, verbose_name='点赞次数')
    liked_count = models.IntegerField(default=0, verbose_name='喜欢次数')
    collected_count = models.IntegerField(default=0, verbose_name='收藏次数')
    commented_count = models.IntegerField(default=0, verbose_name='评论次数')
    up_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
    status = models.CharField(max_length=10, choices=ARTICLE_STATUS, default='0', verbose_name='当前状态')
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-pub_time','id']   # 数据排序
    def __str__(self):
        return "文章标题: {},文章内容: {}".format(self.title, self.content)