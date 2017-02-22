import re
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestDataTests(TestCase):
    fixtures = ['initial_data.json']

    def test_request_reachable(self):
        "Is request page reachable by url name"
        resp = self.client.get(reverse('requests'))
        self.assertEqual(resp.status_code, 200)

    def test_model(self):
        "Is model proprly represents data. Checking by types"
        request = MyHttpRequest(
            method="GET",
            path="/",
            server_protocol="HTTP/1.1",
            status=200,
            response_length=1245
        )
        request.save()
        resp = self.client.get(reverse('requests'))
        pattern = re.compile(
            r'<td>(?P<id>\d+)</td>\W+<td>(?P<method>\w{3,5})</td>'
        )
        target = pattern.search(resp.content)
        # target not found?
        self.assertFalse(target is None)


def test_middleware_works_not_AJAX(self):
        "Is middleware registers requests"
        request = MyHttpRequest.objects.all()
        self.assertEqual(request.count(), 0)
        self.client.get(reverse('requests'))
        response = self.client.get(reverse('requests'))
        request = MyHttpRequest.objects.order_by('date').last()
        self.assertContains(response, request.path, 1)
        request = MyHttpRequest.objects.all()
        # request had been sent 2 times
        self.assertEqual(request.count(), 2)
