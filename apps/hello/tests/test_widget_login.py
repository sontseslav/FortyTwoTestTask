from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):

    def setUp(self):
        "Preparing user for login"
        self.credentials = {
            'username': 'admin',
            'password': 'admin'}
        User.objects.create_user(**self.credentials)

    def test_login_ability(self):
        "If user is able to login: login page exists and accepts name & pass"
        '''Status code is 200 and page accepts correct login and password'''
        response = self.client.get('login')
        self.assertEqual(response.status_code, 200)
        # send login data
        response = self.client.post('login', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)
