from django.urls import path

from content.views import (
    index,
    TopicListView, NewspaperListView, RedactorListView, ArticleListView,
    RedactorDetailView, RedactorCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
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
