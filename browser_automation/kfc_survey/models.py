# coding=utf-8
from django.db import models


class ReceiptParams(models.Model):
    store_number = models.CharField(max_length=5)
    order_number = models.CharField(max_length=4)
    order_datetime = models.DateTimeField()

    automate_settings = models.OneToOneField('AutomateSurveySettings', null=True)


PRECONFIGURED_SETTINGS_TYPE_TUPLE = (
    ('all good', 'All good'),
    ('all medium', 'All medium'),
    ('all bad', 'All bad'),
)


class AutomateSurveySettings(models.Model):
    type = models.CharField(choices=PRECONFIGURED_SETTINGS_TYPE_TUPLE, max_length=20)

    def __unicode__(self):
        return u'{} — {}'.format(self.receiptparams.order_datetime, self.get_type_display())