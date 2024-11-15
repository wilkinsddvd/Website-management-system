from datetime import datetime
from uuid import uuid4
from django.db import models

# Create your models here.

class Author(models.Model):
    GENDER = (
        ('0', '女'),
        ('1', '男'),
    )
    STATUS = (
        ('0', '正常'),
        ('1', '锁定'),
        ('2', '删除'),
    )
    # id =models.AutoField(primary_key=True,verbose_name='作者编号')  # 作者编号
    # username = models.CharField(max_length=50,verbose_name='登录账号')  # 登录账号
    # password = models.CharField(max_length=50,verbose_name='登录密码')  # 登录密码
    # realname = models.CharField(max_length=20,verbose_name='作者姓名')  # 作者姓名
    # age = models.IntegerField(default=0,verbose_name='作者年龄')  # 作者年龄
    # gender = models.CharField(max_length=1,choices=GENDER,verbose_name='性别')  # 性别
    # email = models.EmailField(verbose_name='邮箱')  # 邮箱
    # phone = models.CharField(max_length=20,verbose_name='联系电话')  # 联系电话
    # status = models.CharField(max_length=5,choices=STATUS,verbose_name='用户状态')  # 用户状态
    # intro = models.TextField(verbose_name='个人介绍')  # 个人介绍
    # remark = models.TextField(verbose_name='备注信息')  # 备注信息
    id = models.UUIDField(primary_key=True, verbose_name='作者编号', auto_created=True, default=uuid4)
    username = models.CharField(max_length=50, verbose_name='登录账号',unique=True,db_index=True)
    password = models.CharField(max_length=50, verbose_name='登录密码')
    realname = models.CharField(max_length=20, verbose_name='作者姓名',default='待完善',null=True,blank=True,db_index=True)
    nickname = models.CharField(max_length=20, verbose_name=' 作者昵称',unique=True,null=True,blank=True,db_index=True)
    age = models.IntegerField(default=0, verbose_name='作者年龄')
    gender = models.CharField(max_length=1, choices=GENDER, verbose_name='性别',null=True,blank=True)
    email = models.EmailField(verbose_name='联系邮箱',null=True,blank=True,db_index=True)
    phone = models.CharField(max_length=20, verbose_name='联系电话',db_index=True,null=True,blank=True)
    status = models.CharField(max_length=5, choices=STATUS, default='0', verbose_name='用户状态',help_text='必须选择一个状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    intro = models.TextField(verbose_name='个人介绍',null=True,blank=True)
    remark = models.TextField(verbose_name='备注信息',null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    ''' 自关联 '''
    # authors_liked = models.ManyToManyField('self',  related_name='author') #关注的作者 verbose_name='喜欢的作者' through='AuthorLiked',
    author_liked = models.OneToOneField('self', on_delete=models.SET_NULL,null=True,blank=True) #特别关注的作者 related_name='authors_liked' verbose_name='关注的作者' through='AuthorLiked',
    class Meta:
        verbose_name_plural = '作者'
    def __str__(self):
        return self.realname

class AuthorProfile(models.Model):
    # 用户扩展信息
    id = models.UUIDField(primary_key=True, verbose_name='扩展资料编号', auto_created=True, default=uuid4)
    fans_count = models.IntegerField(default=0, verbose_name='粉丝数')
    visited_count = models.IntegerField(default=0, verbose_name='访问量')
    word_count = models.IntegerField(default=0, verbose_name='文章字数')
    aricle_count = models.IntegerField(default=0, verbose_name='文章数')
    collected_count = models.IntegerField(default=0, verbose_name='收藏数')
    liked_count = models.IntegerField(default=0, verbose_name='喜欢数')
    admired_count = models.IntegerField(default=0, verbose_name='点赞总数')
    author = models.OneToOneField(Author, on_delete=models.CASCADE) # verbose_name='作者'
