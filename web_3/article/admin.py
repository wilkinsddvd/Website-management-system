from django.contrib import admin

from.models import Article   # 引入我们自定义的Article数据类型
admin.site.register(Article)   # 在后台管理系统中注册要管理的数据类型