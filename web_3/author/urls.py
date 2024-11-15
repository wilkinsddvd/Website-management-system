__author__ = 'wilkinsddvd'
__version__ = '1.0'

# 引入依赖的模块
from django.urls import path,include
from . import views

# 路由模块名称
app_name = 'author'

# 添加路由配置
urlpatterns = [
    path('author/', include([
        path('register/', views.author_register, name='register'),
        path('login/', views.author_login, name='login'),
        # path('', views.index, name='index'),
    ])),

    # 11.12修改
    # path('author/register/', views.author_register, name='register'),
    # path('author/login/', views.author_login, name='login'),
    # # 11.12修改
    # path('register/', views.author_register, name='register'),
    # path('login/', views.author_login, name='login'),
]