from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=50)
    jabber = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    other_contacts = models.CharField(max_length=200)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.surname
