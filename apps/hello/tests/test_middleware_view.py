from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestDataTests(TestCase):
    fixtures = ['initial_data.json']

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
