# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Definition'
        db.create_table(u'jisho_definition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'jisho', ['Definition'])

        # Adding model 'VocabularyList'
        db.create_table(u'jisho_vocabularylist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=2048)),
        ))
        db.send_create_signal(u'jisho', ['VocabularyList'])

        # Adding M2M table for field entries on 'VocabularyList'
        m2m_table_name = db.shorten_name(u'jisho_vocabularylist_entries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vocabularylist', models.ForeignKey(orm[u'jisho.vocabularylist'], null=False)),
            ('definition', models.ForeignKey(orm[u'jisho.definition'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vocabularylist_id', 'definition_id'])


    def backwards(self, orm):
        # Deleting model 'Definition'
        db.delete_table(u'jisho_definition')

        # Deleting model 'VocabularyList'
        db.delete_table(u'jisho_vocabularylist')

        # Removing M2M table for field entries on 'VocabularyList'
        db.delete_table(db.shorten_name(u'jisho_vocabularylist_entries'))


    models = {
        u'jisho.definition': {
            'Meta': {'object_name': 'Definition'},
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'jisho.vocabularylist': {
            'Meta': {'object_name': 'VocabularyList'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'entries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'lists'", 'blank': 'True', 'to': u"orm['jisho.Definition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['jisho']