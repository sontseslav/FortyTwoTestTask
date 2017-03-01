# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'hello_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other_contacts', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hello', ['Person'])

<<<<<<< HEAD
        # Adding model 'MyHttpRequest'
        db.create_table(u'hello_myhttprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('server_protocol', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('response_length', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['MyHttpRequest'])

=======
>>>>>>> 0915e9e1c73b39f1dd5550bd77259accc1d3191c

    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'hello_person')

<<<<<<< HEAD
        # Deleting model 'MyHttpRequest'
        db.delete_table(u'hello_myhttprequest')


    models = {
        u'hello.myhttprequest': {
            'Meta': {'ordering': "['-date']", 'object_name': 'MyHttpRequest'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'response_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
=======

    models = {
>>>>>>> 0915e9e1c73b39f1dd5550bd77259accc1d3191c
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_contacts': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hello']