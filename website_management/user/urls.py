from django.urls import path,include
from . import views

# 路由模块名称
app_name = 'user'

# 添加路由配置
urlpatterns = [
    path('user/', include([
        path('register/', views.author_register, name='register'),
        path('login/', views.author_login, name='login'),
        path('logout/', views.user_logout, name='logout'),
        # path('', views.index, name='index'),
    ])),
]