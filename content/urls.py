from django.urls import path

from content.views import (
    index,
    TopicListView, NewspaperListView, RedactorListView, ArticleListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
]

app_name = "content"
