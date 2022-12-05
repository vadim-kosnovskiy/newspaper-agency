from django.urls import path

from content.views import (
    index,
    TopicListView, NewspaperListView, RedactorListView, ArticleListView,
    RedactorDetailView, RedactorCreateView, RedactorDeleteView,
    RedactorUpdateView, TopicDeleteView, TopicUpdateView,
    TopicCreateView, NewspaperDetailView, NewspaperCreateView,
    NewspaperUpdateView, NewspaperDeleteView, ArticleDeleteView,
    ArticleUpdateView, ArticleDetailView, ArticleCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path(
        "articles/create/",
        ArticleCreateView.as_view(),
        name="article-create"
    ),
    path(
        "articles/<int:pk>/detail/",
        ArticleDetailView.as_view(),
        name="article-detail"
    ),
    path(
        "articles/<int:pk>/update/",
        ArticleUpdateView.as_view(),
        name="article-update"
    ),
    path(
        "articles/<int:pk>/delete/",
        ArticleDeleteView.as_view(),
        name="article-delete"
    ),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"),
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"),
    path(
        "newspapers/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),
]

app_name = "content"
