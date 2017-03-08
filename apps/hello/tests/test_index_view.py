# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person


class IndexViewTests(TestCase):

    def test_index_reachable(self):
        """
        Make GET request to 'index', return status 200
        """
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_admin_reachable(self):
        """
        Make GET request to 'admin:index', return status 200
        """
        resp = self.client.get(reverse('admin:index'))
        self.assertEqual(resp.status_code, 200)

    def test_entries_check(self):
        """
        Render "Empty database" if no entries exists, first entry otherwise
        On multiple Person entries exists context contains fields 
        of first entry and template renders it properly
        """
        # no data provided
        resp = self.client.get(reverse('index'))
        self.assertContains(resp, "Empty database")
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
        # context check
        self.assertEquals(resp.context['person'].name, "George")
        self.assertEquals(resp.context['person'].surname, "Petersen")
        self.assertEquals(
            resp.context['person'].date_of_birth, datetime.date(1984, 9, 28)
            )
        self.assertEquals(resp.context['person'].bio, "Some data")
        self.assertEquals(resp.context['person'].email, "aaa@bbb.ccc")
        self.assertEquals(resp.context['person'].jabber, "jabber@domain.com")
        self.assertEquals(resp.context['person'].skype, "test")
        self.assertEquals(
            resp.context['person'].other_contacts, "other contacts"
            )
        self.assertEquals(resp.context['person'].title, "Test title # 1")
        # test template
        self.assertContains(resp, "George")
        self.assertContains(resp, "Petersen")
        self.assertContains(resp, "28.09.1984")
        self.assertContains(resp, "Some data")
        self.assertContains(resp, "aaa@bbb.ccc")
        self.assertContains(resp, "jabber@domain.com")
        self.assertContains(resp, "test")
        self.assertContains(resp, "other contacts")
        self.assertContains(resp, "Test title # 1")

    def test_cyrillic(self):
        """
        Profile view renders cyrillic fields from DB
        """
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

    def test_empty_DB(self):
        """
        On empty DB context passes None
        """
        # DB test - returns none
        self.assertEquals(None, Person.objects.first())
        # context test - passes None to template
        resp = self.client.get(reverse('index'))
        self.assertEquals(None, resp.context['person'])
