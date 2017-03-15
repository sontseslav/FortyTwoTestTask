import re
import datetime
from django.test import TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from apps.hello.models import MyHttpRequest


class RequestDataTests(TestCase):

    def test_request_reachable(self):
        """
        Make GET request to 'requests', return status 200
        """
        resp = self.client.get(reverse('requests'))
        self.assertEqual(resp.status_code, 200)

    def test_view_limit(self):
        """
        View renders only 10 last requests
        """
        for i in range(20):
            self.client.get(reverse('index'))
        requests = MyHttpRequest.objects.all()
        self.assertEqual(requests.count(), 20)
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.context['object_list'].count(), 10)

    def test_model_view(self):
        """
        View renders data in rows, column order is right
        """
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
            r'<td>(?P<method>\w{3,5})</td>\W+<td>/(?P<path>\w+)*</td>'
        )
        target = pattern.search(resp.content)
        # target not found?
        self.assertTrue(target)

    def test_viewed_requests(self):
        """
        View renders only unviewed requests only once
        """
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
        # previous request + 2 generated ones
        self.assertEqual(resp.context['object_list'].count(), 3)
        # previous exist
        self.assertContains(resp, test_path)

    def test_post_template(self):
        """
        POST response template exists, view generates non-empty context
        """
        # If no others requests made - only must POST exists
        self.client.post(reverse('requests'))
        # Checking template for post
        response = render_to_response(
            'hello/post_response.html',
            {'object_list': MyHttpRequest.objects.filter(viewed=False)[:10]},
            content_type="text/html"
            )
        # Is template reachable and processed fine
        self.assertEqual(response.status_code, 200)
        # Is template generated non-empty content
        self.assertNotEqual(response.content, "")

    def test_post_response(self):
        """
        POST response returns new requests

        POST response always has 'object_list' in context,
        'object_list' has max 10 entries
        content-type is html and contains at least one new request,
        markup is consistent with template and has max 10 rows
        """
        # If no others requests made - only must POST exists
        self.client.post(reverse('requests'))
        response = self.client.post(reverse('requests'))
        # object_list not empty
        self.assertTrue(response.context['object_list'])
        pattern = re.compile(
            r'<td>(?P<method>\w{3,5})</td>\W*<td>/(?P<path>\w+)*</td>'
        )
        target = pattern.search(response.content)
        self.assertTrue(target)
        # on many requests
        for x in range(1, 20):
            self.client.get(reverse('index'))
        # sends only 10
        response = self.client.post(reverse('requests'))
        # sends 10 objects in context
        self.assertEqual(len(response.context['object_list']), 10)
        # sends 10 rows in response
        self.assertEqual(response.content.count('<tr>'), 10)
