'''
version v1.0.0
@author: wilkinsddvd
@contact: qingsdao_ddvd@163.com
@software: PyCharm
@file: views.py
'''

from django.shortcuts import render
from django.urls import reverse # 反向解析

def articles_list(request):
    # 查询所有文章
    print("查询所有文章························")
    pass

def articles_author(request, author_id):
    # 查询指定作者的文章：author_id变量会接受路由中传递的数据
    print("查询指定作者的文章····················")
    pass

def articles_liked(request, author_id):
    # 查询指定作者喜欢的文章：author_id变量会接受路由中传递的数据
    print("查询指定作者喜欢的文章·")
    pass

def articles_collected(request,author_id):
    # 查询指定作者收藏的文章：author_id变量会接受路由中传递的数据
    print("查询指定作者收藏的文章···················")
    pass

def articles_year(request, year):
    # 查询指定年份拿到文章：year变量会接受路由中传递的数据
    print("查询指定年份的文章····················")
    pass

def article_month(request, year, month):
    # 查询指定年月份的文章：year、month变量会接受路由中传递的数据
    print("查询指定年月份的文章··················")
    pass

def article_detail(request,article_id):
    # 查询指定文章详情：article_id变量会接受路由中传递的数据
    print("查询指定文章详情·······················")
    pass

# def article_publish(request):
#     # 执行发表文章的代码
#     # new_article = Article() 持久化文章数据
#     # new_article.save()
#     # 直接反向解析，将请求转发到app_name=articl到urlpatterns中name = articl_detail的路由对象
#     return render(reverse('articl:articl_detail'),args=(new_articls.id,))