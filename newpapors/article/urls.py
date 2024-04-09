from . import views
from django.urls import path


app_name = 'article'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('filter/', views.article_filter, name='article_filter'),
    path('article/<int:pk>/update/', views.article_update, name='article_update'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('create_comment/', views.comment_create, name='comment_create')
]