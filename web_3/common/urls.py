from django.urls import path
from . import views

app_name = 'common' #应用名称

urlpatterns = [ #路由匹配
    path('', views.index, name='index'),
]
