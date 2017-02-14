from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexDataTests(TestCase):

    def test_index_reachable(self):
        "is index page reachable by url name"
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
