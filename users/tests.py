from django.urls import reverse
from django.test import TestCase


class IndexPageTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
