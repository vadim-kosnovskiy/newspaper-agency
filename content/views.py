from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .forms import (ArticleNewspaperSelectForm, ArticleTopicSelectForm,
                    TopicSearchForm, NewspaperSearchForm, RedactorSearchForm
                    )
from .models import Redactor, Newspaper, Topic, Article


@login_required
def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    num_articles = Article.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_articles": num_articles,
        "num_visits": num_visits + 1,
    }

    return render(request, "content/index.html", context=context)


class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    paginate_by = 5
    queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)

        topic_id = self.request.GET.get("topic_id", "")
        context["article_topic_select"] = ArticleTopicSelectForm(
            initial={"topic_id": topic_id}
        )
        newspaper_id = self.request.GET.get("newspaper_id", "")
        context["article_newspaper_select"] = ArticleNewspaperSelectForm(
            initial={"newspaper_id": newspaper_id}
        )

        return context

    def get_queryset(self):
        topic_id = self.request.GET.get("topic_id", "")
        newspaper_id = self.request.GET.get("newspaper_id", "")
        if topic_id:
            self.queryset = self.queryset.filter(topic__id=topic_id)
        if newspaper_id:
            self.queryset = self.queryset.filter(newspaper__id=newspaper_id)

        return self.queryset


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "content/topic_list.html"
    paginate_by = 5
    queryset = Topic.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        context["topic_search"] = TopicSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        name = self.request.GET.get("name", "")
        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")
        context["newspaper_search"] = NewspaperSearchForm(
            initial={"title": title},
        )

        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                title__icontains=form.cleaned_data["title"])

        return self.queryset


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5
    queryset = Redactor.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username")
        context["redactor_search"] = RedactorSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        form = RedactorSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"])

        return self.queryset


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorDetailView, self).get_context_data(**kwargs)
        context["num_newspapers"] = Newspaper.objects.filter(publishers__id=self.kwargs["pk"]).count()
        return context
