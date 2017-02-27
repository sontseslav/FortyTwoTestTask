import re
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestModelTests(TestCase):
    fixtures = ['initial_data.json']

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
