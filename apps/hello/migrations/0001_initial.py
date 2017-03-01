# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MyHttpRequest.viewed'
        db.add_column(u'hello_myhttprequest', 'viewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MyHttpRequest.viewed'
        db.delete_column(u'hello_myhttprequest', 'viewed')


    models = {
        u'hello.myhttprequest': {
            'Meta': {'ordering': "['-date']", 'object_name': 'MyHttpRequest'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'response_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
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
