"""personal_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,register_converter
from .route_converter import RouteYearConverter

# 注册年份类型转换器
register_converter(RouteYearConverter, 'yyyy')
urlpatterns = [
    path('admin/', admin.site.urls),    # 后台管理模块
    # path('', include('common.urls')), # 公共模块
    path('', include('author.urls')),  # 用户模块
    path('', include('article.urls')), # 文章模块

    # path('',include('comment.urls')), # 评论模块
    # path('', include('album.urls')), # 相册模块
    # path('', include('message.urls')), # 留言模块
    # 11.15.2024 新增 但后三个模块暂时不用，先注释掉


    # path('',include('article.urls')), # 文章模块
    # path('', include('comment.urls')), # 评论模块
    # path('', include('album.urls')), # 相册模块
    # path('', include('message.urls')), # 留言模块
    # path('author/', include('author.urls')),
]

# handler400 = 'common.views.page400error' # 全局400页面
# handler404 = 'common.views.page400error' # 全局404页面
# handler403 = 'common.views.page403error' # 全局403页面
# handler500 = 'common.views.page500error' # 全局500页面