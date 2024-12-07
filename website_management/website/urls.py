from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path('website/', include([
        path('add/', views.add_website, name='add'),
        path('delete/<int:web_id>/', views.delete_website, name='delete'),
        path('edit/<int:web_id>/', views.edit_website, name='edit'),
        path('', views.list_websites, name='list'),
    ])),
]

