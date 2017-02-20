import re
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import HttpRequest


class RequestDataTests(TestCase):
    fixtures = ['initial_data.json']

    def test_request_reachable(self):
        "Is request page reachable by url name"
        request = HttpRequest.objects.all()
        for i in request:
            i.delete()
        resp = self.client.get(reverse('requests'))
        self.assertEqual(resp.status_code, 200)

    def test_hardcorded_data(self):
        "Is request page has specified data/not empty"
        resp = self.client.get(reverse('requests'))
        self.assertTrue('<h4>Empty database!</h4>' not in resp.content)

    def test_model(self):
        "Is model proprly represents data. Checking by types"
        resp = self.client.get(reverse('requests'))
        pattern = re.compile(
            r'<td>(?P<id>\d+)</td>\W+<td>(?P<method>\w{3,5})</td>'
        )
        target = pattern.search(resp.content)
        # target not found?
        self.assertFalse(target is None)

    def test_middleware_works(self):
        "Is middleware registers requests"
        # Purge DB?
        request = HttpRequest.objects.all()
        self.assertEqual(request.count(), 0)
        response = self.client.get(reverse('requests'))
        request = HttpRequest.objects.order_by('date').last()
        # Catch path
        self.assertContains(response, request.path, 1)
        # Is request was only one?
        request = HttpRequest.objects.all()
        self.assertEqual(request.count(), 0)
