from django.test import TestCase
from django.core.urlresolvers import reverse
from hello.models import Person


class IndexViewTests(TestCase):

    def test_empty_DB(self):
        "If DB empty"
        # DB test - returns none
        self.assertTrue(Person.objects.exists())
        # context test - passes None to template
        resp = self.client.get(reverse('index'))
        self.assertEquals(None, resp.context['person'])
