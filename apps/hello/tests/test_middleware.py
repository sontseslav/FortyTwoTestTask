from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestMiddlewareTests(TestCase):
    fixtures = ['initial_data.json']

    def test_middleware_works(self):
        "Is middleware registers requests"
        request = MyHttpRequest.objects.all()
        self.assertEqual(request.count(), 0)
        self.client.get(reverse('requests'))
        response = self.client.get(reverse('requests'))
        request = MyHttpRequest.objects.order_by('date').last()
        self.assertContains(response, request.path, 2)
        request = MyHttpRequest.objects.all()
        # request had been sent 2 times
        self.assertEqual(request.count(), 2)
