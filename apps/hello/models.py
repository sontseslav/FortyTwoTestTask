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

    def __unicode__(self):
        return self.name + " " + self.surname


class HttpRequest(models.Model):
    method = models.CharField(max_length=7)
    path = models.CharField(max_length=255)
    server_protocol = models.CharField(max_length=12)
    status = models.PositiveSmallIntegerField()
    response_length = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return self.method + " " + self.path
