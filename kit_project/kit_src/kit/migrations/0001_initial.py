# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Config'
        db.create_table('kit_config', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('kit', ['Config'])


    def backwards(self, orm):
        # Deleting model 'Config'
        db.delete_table('kit_config')


    models = {
        'kit.config': {
            'Meta': {'object_name': 'Config'},
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['kit']