from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('list/', views.news_list, name='news_list'),
    path('create/', views.create_announcement, name='create_announcement'),
    path('edit/<int:id>/', views.edit_announcement, name='edit_announcement'),
    path('delete/<int:id>/', views.delete_announcement, name='delete_announcement'),
]
