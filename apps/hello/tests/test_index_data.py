from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person


class IndexDataTests(TestCase):
    fixtures = ['initial_data.json']

    def test_index_reachable(self):
        "is index page reachable by url name"
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_admin_reachable(self):
        "is index page reachable by url name"
        resp = self.client.get(reverse('admin:index'))
        self.assertEqual(resp.status_code, 200)

    def test_index_hardcoded_data(self):
        "is view returning hardcoded data"
        resp = self.client.get(reverse('index'))
        self.assertTrue('42 Coffee Cups Test Assignment' in resp.content)
        self.assertTrue('Stanislav' in resp.content)
        self.assertTrue('Khvalinsky' in resp.content)
        self.assertTrue('s.khvalinsky@gmail.com' in resp.content)
        self.assertTrue(
            'stanislav_khvalinsky@42cc.co' in resp.content
        )
        self.assertTrue('28.09.1984' in resp.content)
        self.assertTrue('still.hope' in resp.content)
        self.assertEqual(2, resp.content.count('Don\'t be disclosed'))

    def test_person_model(self):
        "is model provides correct data"
        resp = self.client.get(reverse('index'))
        try:
            person = Person.objects.all()[:1][0]
        except Person.DoesNotExist:
            raise AssertionError("Person entity with id 1 does not exisits")
        self.assertContains(resp, person.name)
        self.assertContains(resp, person.surname)
        date = person.date_of_birth.ctime()
        date = '.'.join(date.split('-')[:-1])
        self.assertContains(resp, date)
        self.assertContains(resp, person.bio)
        self.assertContains(resp, person.email)
        self.assertContains(resp, person.jabber)
        self.assertContains(resp, person.skype)
        self.assertContains(resp, person.other_contacts)
        self.assertContains(resp, person.title)
