import re
import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestDataTests(TestCase):

    def test_request_reachable(self):
        "Is request page reachable by url name"
        resp = self.client.get(reverse('requests'))
        self.assertEqual(resp.status_code, 200)

    def test_view_limit(self):
        "Is request page shows only 10 last requests"
        for i in range(20):
            self.client.get(reverse('index'))
        requests = MyHttpRequest.objects.all()
        self.assertEqual(requests.count(), 20)
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.context['object_list'].count(), 10)

    def test_model_view(self):
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

    def test_viewed_requests(self):
        "Is viewed requests displayed?"
        test_path = "/test"
        request = MyHttpRequest(
            method="GET",
            path=test_path,
            server_protocol="HTTP/1.1",
            status=200,
            response_length=1245,
            date=datetime.datetime.now(),
            viewed=False
        )
        request.save()
        request = MyHttpRequest(
            method="GET",
            path=test_path,
            server_protocol="HTTP/1.1",
            status=200,
            response_length=1245,
            date=datetime.datetime.now(),
            viewed=False
        )
        request.save()
        resp = self.client.get(reverse('requests'))
        self.assertEqual(resp.context['object_list'].count(), 2)
        self.assertContains(resp, test_path)
        resp = self.client.get(reverse('requests'))
        # privious request
        self.assertEqual(resp.context['object_list'].count(), 1)
        self.assertNotContains(resp, test_path)
