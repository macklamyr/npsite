from django.contrib import admin
from django.urls import path
from .views import PostList, SearchList, PostDetail, PostCreate, PostUpdate, PostDelete, ArticlesCreate

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', SearchList.as_view(), name='search'),
    path('news/create/', PostCreate.as_view(), name='create_news'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='update_news'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete_news'),
    path('articles/create/', ArticlesCreate.as_view(), name='create_articles'),
    path('articles/<int:pk>/update/', PostUpdate.as_view(), name='update_articles'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='delete_articles'),
]