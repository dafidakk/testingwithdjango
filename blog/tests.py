from turtle import title
from unicodedata import name
from django.test import TestCase
from . models import Question, Choice, Post 
# Create your tests here.


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create("django_test", "fatih", "post")

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), "django_test")
