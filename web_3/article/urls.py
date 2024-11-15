__author__ = 'wilkinsddvd'
__version__ = '1.0'

# 引入依赖的模块
from django.urls import path,include,re_path
from . import views

# 路由模块名称
app_name = 'article'

# 添加路由配置
urlpatterns = [
    path('article/',include([
        path('', views.articles_list, name='articles_list'),

        # 11.15修改 下列两行存在问题，暂时注释掉
        # path('/<yyyy:year>/', views.articles_year,name='articles_year'),  # 根据年份获取文章列表
        # path('/<yyyy:year>/<int:month>/', views.article_month),  # 根据年月获取文章列表

        path('<uuid:author_id>/', views.articles_author, name='articles_author'),  # 根据作者ID获取文章列表
        path('<uuid:author_id>/liked/', views.articles_liked, name='articles_liked'),
        path('<uuid:author_id>/collected/', views.articles_collected, name='articles_collected'),
        path('<uuid:author_id>/detail/', views.article_detail, name='article_detail'),
    ]))
        # 11.15修改
        # path('',views.articles_list,name='articles_list'),
        # path('<int:year>/', views.articles_year),  # 根据年份获取文章列表
        # path('<int:year>/<int:month>/',views.article_month),    # 根据年月获取文章列表
        # path('<uuid:author_id>/',views.articles_author,name='articles_author'), # 根据作者ID获取文章列表
        # path('<uuid:author_id>/liked/',views.articles_liked,name='articles_liked'),
        # path('<uuid:author_id>/collected/',views.articles_collected,name='articles_collected'),
        # path('<uuid:author_id>/detail/',views.article_detail,name='article_detail'),


    # 11.15修改
    # path('article_list/',views.article_list),
    # path('article_year/<int:year>/',views.article_year),    # 根据年份获取文章列表
    # path('article_month/<int:year>/<int:month>/',views.article_month), # 根据年月获取文章列表
    # path('articl/<int:article_id>/',views.article_detail), # 根据文章ID获取文章详情

    # 11.15修改
    # re_path('^article/(?P<year>\d{4})/$', views.article_year, name='article_year'),
    # re_path('^article_month/(?P<year>\d{4})/(?P<month>\d{2})/$', views.article_month, name='article_month'),
    # re_path('^article_detail/(?P<article_id>\S{10,})/$', views.article_detail, name='article_detail')

    # 11.12修改
    # path('author/register/', views.author_register, name='register'),
    # path('author/login/', views.author_login, name='login'),
    # # 11.12修改
    # path('register/', views.author_register, name='register'),
    # path('login/', views.author_login, name='login'),
    # 11.14修改
    # path('author/', include([
    #     path('register/', views.author_register, name='register'),
    #     path('login/', views.author_login, name='login'),
    #     # path('', views.index, name='index'),
    # ])),
]