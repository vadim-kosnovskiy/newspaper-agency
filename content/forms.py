from django import forms

from content.models import Newspaper, Topic


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by newspaper.."})
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username.."}
        )
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by topic.."}
        )
    )


class ArticleTopicSelectForm(forms.Form):
    queryset = Topic.objects.all()
    topic_choices = [(inst.id, inst) for inst in queryset]
    topic_choices.append(("", "-- select topic --"))
    topic_id = forms.ChoiceField(
        choices=topic_choices,
        label="",
    )


class ArticleNewspaperSelectForm(forms.Form):
    queryset = Newspaper.objects.all()
    newspaper_choices = [(inst.id, inst) for inst in queryset]
    newspaper_choices.append(("", "-- select newspaper"))
    newspaper_id = forms.ChoiceField(
        choices=newspaper_choices,
        label="",
    )
