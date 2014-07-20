# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReceiptParams'
        db.create_table(u'kfc_survey_receiptparams', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store_number', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('order_number', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('order_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('validation_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('automate_settings', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kfc_survey.AutomateSurveySettings'], unique=True, null=True)),
        ))
        db.send_create_signal(u'kfc_survey', ['ReceiptParams'])

        # Adding model 'AutomateSurveySettings'
        db.create_table(u'kfc_survey_automatesurveysettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'kfc_survey', ['AutomateSurveySettings'])


    def backwards(self, orm):
        # Deleting model 'ReceiptParams'
        db.delete_table(u'kfc_survey_receiptparams')

        # Deleting model 'AutomateSurveySettings'
        db.delete_table(u'kfc_survey_automatesurveysettings')


    models = {
        u'kfc_survey.automatesurveysettings': {
            'Meta': {'object_name': 'AutomateSurveySettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'kfc_survey.receiptparams': {
            'Meta': {'object_name': 'ReceiptParams'},
            'automate_settings': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kfc_survey.AutomateSurveySettings']", 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'store_number': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'validation_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['kfc_survey']