from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase

from django.test import TestCase
from .models import post
class PostModelTest(TestCase):
 def setUp(self):
  post.objects.create(text='just a test')
def test_text_content(self):
 post=post.objects.get(id=1)
 expected_object_name = f'{post.text}'
 self.assertEqual(expected_object_name, 'just a test')