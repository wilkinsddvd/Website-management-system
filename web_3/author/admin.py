from django.contrib import admin

from.models import Author   # 引入我们自定义的Author类型
admin.site.register(Author)   # 在后台管理系统中注册要管理的数据类型
