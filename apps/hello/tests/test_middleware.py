from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestMiddlewareTests(TestCase):

    def test_middleware_works(self):
        "Is middleware registers requests - 2 requests creates 2 entries in DB"
        request = MyHttpRequest.objects.all()
        self.assertEqual(request.count(), 0)
        self.client.get(reverse('requests'))
        response = self.client.get(reverse('requests'))
        # reverse initial order
        request = MyHttpRequest.objects.order_by('date').last()
        self.assertContains(response, request.path, 2)
        request = MyHttpRequest.objects.all()
        # request had been sent 2 times
        self.assertEqual(request.count(), 2)
