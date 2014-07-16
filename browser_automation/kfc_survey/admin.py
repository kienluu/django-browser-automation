from django.contrib import admin
from kfc_survey.models import ReceiptParams, AutomateSurveySettings


class InlineReceiptParamsAdmin(admin.StackedInline):
    model = ReceiptParams


class AutomateSurveySettingsAdmin(admin.ModelAdmin):
    inlines = [InlineReceiptParamsAdmin]


admin.site.register(AutomateSurveySettings, AutomateSurveySettingsAdmin)