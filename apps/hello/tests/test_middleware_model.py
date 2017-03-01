import datetime
from django.test import TestCase
from apps.hello.models import MyHttpRequest


class RequestModelTests(TestCase):
    '''look to the test from t1_mockup'''

    def test_model(self):
        "Is model constructed proprly"
        request = MyHttpRequest(
            method="GET",
            path="/",
            server_protocol="HTTP/1.1",
            status=200,
            response_length=1245,
            date=datetime.datetime.now(),
            viewed=False
        )
        self.assertEqual(
            str(request),
            request.date.strftime("%d/%b/%Y %H:%M:%S")
            + " " + request.method
            + " " + request.path
            + " viewed: " + str(request.viewed)
            )
        self.assertTrue(
            type(request.date) is datetime.datetime
            and type(request.method) is str
            and type(request.viewed) is bool
            )
        self.assertEqual(str(MyHttpRequest._meta.ordering), "['-date']")
