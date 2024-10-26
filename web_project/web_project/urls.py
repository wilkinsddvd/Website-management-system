# from django.conf.urls import url 已废弃
from django.urls import re_path as url
from . import views, testdb, search, search2
from django.contrib import admin

urlpatterns = [
    # url(r'^hello/$', views.hello),
    url(r'^runoob/$', views.runoob),
    url(r'^testdb/$', testdb.testdb),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
    url(r'^admin/', admin.site.urls), # 管理后台
]

# from django.conf.urls import url  已废弃
# from django.urls import re_path as url
# from . import views, testdb, search
#
# urlpatterns = [
#     url(r'^hello/$', views.runoob),
#     url(r'^testdb/$', testdb.testdb),
#     url(r'^search-form/$', search.search_form),
#     url(r'^search/$', search.search),
# ]
# from django.urls import path
#
# from . import views, testdb
#
# urlpatterns = [
#     path('runoob/', views.runoob),
#     path('testdb/', testdb.testdb),
# ]

# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('hello/', views.hello, name="hello"),
# ]
# from django.urls import include, re_path

# urlpatterns = [
#     re_path(r'^index/$', views.index, name='index'),
#     re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
#     re_path(r'^weblog/', include('blog.urls')),
#     ...
# ]