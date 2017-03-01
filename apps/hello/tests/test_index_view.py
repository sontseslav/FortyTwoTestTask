# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person


class IndexViewTests(TestCase):
    fixtures = ['initial_data.json']

    def test_index_reachable(self):
        "Is index page reachable by url name"
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_admin_reachable(self):
        "Is index page reachable by url name"
        resp = self.client.get(reverse('admin:index'))
        self.assertEqual(resp.status_code, 200)

    def test_entries_check(self):
        "What if no person or two persons"
        # no data provided
        resp = self.client.get(reverse('index'))
        self.assertContains(resp, "No etntry exists")
        # two entries added
        for i in range(2):
            person = Person(
                name="George",
                surname="Petersen",
                date_of_birth="1984-09-28",
                bio="Some data",
                email="aaa@bbb.ccc",
                jabber="jabber@domain.com",
                skype="test",
                other_contacts="other contacts",
                title="Test title # " + str(i+1)
            )
            person.save()
        resp = self.client.get(reverse('index'))
        # only first displayed
        self.assertContains(resp, "Test title # 1")

    def test_cyrillic(self):
        "If DB has cyrillic strings"
        person = Person(
            name=u"Іван",
            surname=u"Іваненко",
            date_of_birth="1984-09-28",
            bio=u"Щось",
            email="aaa@bbb.ccc",
            jabber="jabber@domain.com",
            skype=u"test",
            other_contacts=u"Ще щось",
            title=u"Тест"
            )
        person.save()
        resp = self.client.get(reverse('index'))
        self.assertContains(resp, u"Тест")
