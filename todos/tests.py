from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):

    def setUp(self):
        Todo.objects.create(title='first todo')
        Todo.objects.create(description='a description here')

    def test_title_content(self):
        todo=Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first todo')

    def test_desctiption_content(self):
        todo=Todo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEqual(expected_object_name, 'a description here')