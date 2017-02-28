from django.test import TestCase
from apps.hello.models import Person


class IndexModelTests(TestCase):

    def test_model(self):
        "Is model constructed properly"
        person = Person(
            name="George",
            surname="Petersen",
            date_of_birth="1984-09-28",
            bio="Some data",
            email="aaa@bbb.ccc",
            jabber="jabber@domain.com",
            skype="test",
            other_contacts="other contacts",
            title="title"
        )
        self.assertEqual(str(person), person.name + " " + person.surname)
        self.assertTrue(type(person.name) is str and
                        type(person.surname) is str)
        self.assertEqual(str(Person._meta.verbose_name_plural), "persons")
