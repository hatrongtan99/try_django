from django.urls import path
from .views import ListArticle, DetailArticle, CreateArticle, UpdateArticle

app_name = "article"

urlpatterns = [
    path("", ListArticle.as_view(), name="article-list"),
    path("detail/<int:id>/", DetailArticle.as_view(), name="article-detail"),
    path("create/", CreateArticle.as_view(), name="create-article"),
    path("update/<int:id>/", UpdateArticle.as_view(), name="update-article")
]
