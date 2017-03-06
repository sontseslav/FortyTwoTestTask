import datetime
from django.test import TestCase
from apps.hello.models import MyHttpRequest


class RequestModelTests(TestCase):

    def test_model(self):
        "Is model constructed properly: right object output, field types"
        '''str() method is overrided, string fields had str type(),
        boolean - bool, ordering by date descending'''
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
