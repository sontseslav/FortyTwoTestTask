from django.test import TestCase
from django.core.urlresolvers import reverse


class RequestDataTests(TestCase):
    fixtures = ['initial_data.json']

    def test_request_reachable(self):
        "is request page reachable by url name"
        resp = self.client.get(reverse('requests'))
        self.assertEqual(resp.status_code, 200)

    def test_hardcorded_data(self):
        "is request page has specified data"
        resp = self.client.get(reverse('requests'))
        self.assertTrue('<h4>Empty database!</h4>' not in resp.content)
