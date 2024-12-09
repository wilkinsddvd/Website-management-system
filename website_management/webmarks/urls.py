# urls.py
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('bookmarks/', include([
        path('', views.bookmark_list, name='bookmark_list'),
        path('add/', views.add_bookmark, name='add_bookmark'),
        path('delete/<int:bookmark_id>/', views.delete_bookmark, name='delete_bookmark'),
    ])),
]