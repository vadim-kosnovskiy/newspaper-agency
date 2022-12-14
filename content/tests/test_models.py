from django.test import TestCase

from content.models import Redactor, Newspaper, Topic, Article


class ModelsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Redactor.objects.create(
            first_name="Matthew",
            last_name="Kaminski",
            years_of_experience="28"
        )

        Topic.objects.create(
            name="Politics")

    def test_redactor_model_str(self):
        redactor = Redactor.objects.create(
            username="matthew.kaminski",
            first_name="Matthew", last_name="Kaminski")
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_get_absolute_url(self):
        redactor = Redactor.objects.get(id=1)
        self.assertEqual(redactor.get_absolute_url(), "/redactors/1/")

    def test_topic_name_str(self):
        topic = Topic.objects.get(id=1)
        self.assertEqual(
            str(topic), f"{topic.name}"
        )

    def test_newspaper_title_str(self):
        newspaper = Newspaper.objects.create(
            title="Politico",
        )
        self.assertEqual(
            str(newspaper), f"{newspaper.title}"
        )

    def test_article_title_str(self):
        topic = Topic.objects.get(id=1)
        article = Article.objects.create(
            article_title="test_article_title",
            topic=topic
        )
        self.assertEqual(str(article), article.article_title)
