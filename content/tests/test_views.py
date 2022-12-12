from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from content.models import Redactor, Newspaper, Topic, Article


class PublicRedactorTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(reverse("content:redactor-list"))

        self.assertNotEqual(resp.status_code, 200)


class PublicNewspaperTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(reverse("content:newspaper-list"))

        self.assertNotEqual(resp.status_code, 200)


class PublicTopicTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(reverse("content:topic-list"))

        self.assertNotEqual(resp.status_code, 200)


class PublicArticleTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(reverse("content:article-list"))

        self.assertNotEqual(resp.status_code, 200)


class ViewsTests(TestCase):
    def setUp(self) -> None:
        number_of_articles = 10

        for article_id in range(number_of_articles):
            topic = Topic.objects.create(
                name=f"Name {article_id}",
            )

            newspaper = Newspaper.objects.create(
                title=f"Title {article_id}",
            )

            Article.objects.create(
                article_title=f"Article_title {article_id}",
                topic=topic,
                newspaper=newspaper
            )

            Redactor.objects.create(
                username=f"username {article_id}",
                years_of_experience="22"
            )

        self.redactor = get_user_model().objects.create_user(
            "test_user",
            "password123"
        )
        self.client.force_login(self.redactor)

    def test_redactor_get_context_data(self) -> None:
        response = self.client.get(reverse("content:redactor-list") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["redactor_list"]), 5)
        self.assertTrue("redactor_search" in response.context)
        self.assertTrue(
            "username" in response.context["redactor_search"].fields
        )

    def test_newspaper_get_context_data(self) -> None:
        response = self.client.get(
            reverse("content:newspaper-list") + "?page=2"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["newspaper_list"]), 5)
        self.assertTrue("newspaper_search" in response.context)
        self.assertTrue(
            "title" in response.context["newspaper_search"].fields
        )

    def test_topic_get_context_data(self) -> None:
        response = self.client.get(
            reverse("content:topic-list") + "?page=2"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["topic_list"]), 5)
        self.assertTrue("topic_search" in response.context)
        self.assertTrue(
            "name" in response.context["topic_search"].fields
        )

    def test_article_get_context_data(self) -> None:
        response = self.client.get(reverse("content:article-list") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["article_list"]), 5)
        self.assertTrue("article_topic_select" in response.context)
        self.assertTrue("topic_id" in response.context["article_topic_select"].fields)

    def test_redactor_get_queryset(self) -> None:
        response = self.client.get("/redactors/?username=test")
        self.assertQuerysetEqual(
            response.context["redactor_list"],
            Redactor.objects.filter(username__icontains="test")
        )

    def test_newspaper_get_queryset(self) -> None:
        response = self.client.get("/newspapers/?title=test")
        self.assertQuerysetEqual(
            response.context["newspaper_list"],
            Newspaper.objects.filter(title__icontains="test")
        )

    def test_topic_get_queryset(self) -> None:
        response = self.client.get("/topics/?name=test")
        self.assertQuerysetEqual(
            response.context["topic_list"],
            Topic.objects.filter(name__icontains="test")
        )

    def test_article_topic_get_queryset(self) -> None:
        response = self.client.get("/articles/?topic_id=1")
        self.assertQuerysetEqual(
            response.context["article_list"],
            Article.objects.filter(topic__id=1)
        )

    def test_article_newspaper_get_queryset(self) -> None:
        response = self.client.get("/articles/?newspaper_id=1")
        self.assertQuerysetEqual(
            response.context["article_list"],
            Article.objects.filter(newspaper__id=1)
        )
