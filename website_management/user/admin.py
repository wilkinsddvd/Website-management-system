from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username', 'password')
    list_filter = ('username', 'password')


'''新增内容'''
# from django.contrib import admin
# from .models import User
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_joined', 'is_staff')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_active')






# from django.contrib import admin
# from .models import User
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_joined', 'is_staff')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_active')