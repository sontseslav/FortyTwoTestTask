from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person


class IndexViewTests(TestCase):

    def test_index_reachable(self):
        "Is index page reachable by url name"
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_admin_reachable(self):
        "Is index page reachable by url name"
        resp = self.client.get(reverse('admin:index'))
        self.assertEqual(resp.status_code, 200)

    def test_model_representation(self):
        "Is model provides correct data"
        resp = self.client.get(reverse('index'))
        person = Person.objects.first()
        self.assertTrue(person != None)
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

    def test_entries_count(self):
        "Is person only one"
        counter = Person.objects.all().count()
        print Person.objects.all()
        print counter
        self.assertTrue(counter == 1)

    def test_cyrillic(self):
        "Is DB has cyrillic strings"
        persons = Person.objects.all()
        for p in persons:
            for f in p._meta.get_all_field_names():
                field = getattr(p, f, None)
                try:
                    str(field).decode('ascii')
                except UnicodeDecodeError:
                    raise AssertionError("Cyrillic fields not allowed")