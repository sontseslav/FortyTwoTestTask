from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person


class IndexModelTests(TestCase):
    fixtures = ['initial_data.json']


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
