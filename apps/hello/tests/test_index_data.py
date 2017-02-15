from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexDataTests(TestCase):

    def test_index_reachable(self):
        "is index page reachable by url name"
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_admin_reachable(self):
        "is index page reachable by url name"
        resp = self.client.get(reverse('admin:index'))
        self.assertEqual(resp.status_code, 200)

    def test_index_hardcoded_data(self):
        "is view returning hardcoded data"
        resp = self.client.get(reverse('index'))
        self.assertTrue('42 Coffee Cups Test Assignment' in resp.content)
        self.assertTrue('Stanislav' in resp.content)
        self.assertTrue('Khvalinsky' in resp.content)
        self.assertTrue('s[dot]khvalinsky[at]gmail[dot]com' in resp.content)
        self.assertTrue(
            'Jabber: Stanislav_Khvalinsky[at]42cc[dot]co' in resp.content
        )
        self.assertTrue('28.09.1984' in resp.content)
        self.assertTrue('still[dot]hope' in resp.content)
        self.assertEqual(2, resp.content.count('Don\'t be disclosed'))
