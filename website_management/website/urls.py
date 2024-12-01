from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path('website/', include([
    path('add/', views.add_website, name='add'),
    path('delete/<int:website_id>/', views.delete_website, name='delete'),
    path('', views.list_websites, name='list'),
    ])),
]

