from django.contrib import admin
from .models import Website

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'description', )
    search_fields = ('url', 'description')
    list_filter = ('url','description')

''' 下面和上面都是新增内容,测试没过'''
# from django.contrib import admin
# from .models import Website
#
# @admin.register(Website)
# class WebsiteAdmin(admin.ModelAdmin):
#     list_display = ('url', 'description', 'created_at')
#     search_fields = ('url', 'description')
#     list_filter = ('created_at',)




# from django.contrib import admin
# from .models import Website
#
# @admin.register(Website)
# class WebsiteAdmin(admin.ModelAdmin):
#     list_display = ('url', 'description')
#     search_fields = ('url', 'description')
#     # list_filter = ('url',)