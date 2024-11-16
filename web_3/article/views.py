'''
version v1.0.0
@author: wilkinsddvd
@contact: qingsdao_ddvd@163.com
@software: PyCharm
@file: views.py
'''

from django.shortcuts import render, redirect,get_object_or_404,get_list_or_404 # 反向解析
from django.urls import reverse # 反向解析
import article
from article.models import Article
from django.views.decorators.gzip import gzip_page # 11.16 压缩响应
from author.models import Author


# 11.16 重构根据编号查询文章的视图处理函数
# 11.16 更新_2
@gzip_page # 11.16 压缩响应
def article_detail(request,article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/articles.html',
                  {'res_code':200,'res_msg':'查看文章详情', 'article': article})
    # article = Article.objects.get(id=article_id) 11.16 注释掉
    # return redirect(article) 11.16 注释掉
    # 查询指定文章详情：article_id变量会接受路由中传递的数据
    #  rint("查询指定文章详情·······················")
    # pass

@gzip_page # 压缩响应
def articles_author(request, author_id):
    ''' 查询指定作者的所有文章'''
    author = get_object_or_404(Author, pk=author_id)
    articles = author.article_set.all()
    return render(request, 'article/articles.html',
                  {'res_code':'200', 'res_msg':'查询作者的所有文章',  'articles':articles})# 11.16 完善 author/views.py

@gzip_page # 11.16 压缩响应
def articles_list(request,status=1):
    # 查询所有文章
    articles = get_list_or_404(Article)
    return render(request, 'article/articles.html',
                  {'res_code': 200, 'res_msg':'查询所有文章', articles: articles})
    # print("查询所有文章························")
    # pass

def articles_year(request, year):
    # 查询指定年份拿到文章：year变量会接受路由中传递的数据
    articles = get_list_or_404(Article, pub_time__year=year)
    return render(request, 'article/articles.html', {'articles': articles})
    # print("查询指定年份的文章····················")
    # pass

def article_month(request, year, month):
    # 查询指定年月份的文章：year、month变量会接受路由中传递的数据
    articles = get_list_or_404(Article, pub_time__year=year, pub_time__month=month)
    return render(request, 'article/articles.html', {'articles': articles})
    # print("查询指定年月份的文章··················")
    # pass

# def articles_author(request, author_id):
#     pass
#     # 查询指定作者的文章：author_id变量会接受路由中传递的数据
#     # print("查询指定作者的文章····················")
#     # pass

def articles_liked(request, author_id):
    # 查询指定作者喜欢的文章：author_id变量会接受路由中传递的数据
    print("查询指定作者喜欢的文章·")
    pass

def articles_collected(request,author_id):
    # 查询指定作者收藏的文章：author_id变量会接受路由中传递的数据
    print("查询指定作者收藏的文章···················")
    pass


def article_publish(request):
    # 执行发表文章的代码
    return redirect('article:article_detail',article_id = article.id)

# 还有一种方法实现上述发表文章，但是是通过硬编码路径实现跳转,代码如下：
# def article_publish(request):
#     # 执行发表文章的代码
#     to = 'article/' + article.id + '/detail/'
#     return redirect(to)

# 11.16 更新前的内容，暂时注释掉
# def articles_list(request):
#     # 查询所有文章
#     print("查询所有文章························")
#     pass
#
# def articles_author(request, author_id):
#     # 查询指定作者的文章：author_id变量会接受路由中传递的数据
#     print("查询指定作者的文章····················")
#     pass
#
# def articles_liked(request, author_id):
#     # 查询指定作者喜欢的文章：author_id变量会接受路由中传递的数据
#     print("查询指定作者喜欢的文章·")
#     pass
#
# def articles_collected(request,author_id):
#     # 查询指定作者收藏的文章：author_id变量会接受路由中传递的数据
#     print("查询指定作者收藏的文章···················")
#     pass
#
# def articles_year(request, year):
#     # 查询指定年份拿到文章：year变量会接受路由中传递的数据
#     print("查询指定年份的文章····················")
#     pass
#
# def article_month(request, year, month):
#     # 查询指定年月份的文章：year、month变量会接受路由中传递的数据
#     print("查询指定年月份的文章··················")
#     pass
#
# def article_detail(request,article_id):
#     # 查询指定文章详情：article_id变量会接受路由中传递的数据
#     # print("查询指定文章详情·······················")
#     pass

# 11.15 更新，反向解析，但是不完善，暂时注释掉
# def article_publish(request):
#     # 执行发表文章的代码
#     # new_article = Article() 持久化文章数据
#     # new_article.save()
#     # 直接反向解析，将请求转发到app_name=articl到urlpatterns中name = articl_detail的路由对象
#     return render(reverse('articl:articl_detail'),args=(new_articls.id,))