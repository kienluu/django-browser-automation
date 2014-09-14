from django.contrib import admin
from kfc_survey.models import ReceiptParams, AutomateSurveySettings
from kfc_survey.tasks import FillOutKfcSurveyForms


class InlineReceiptParamsAdmin(admin.StackedInline):
    model = ReceiptParams


class AutomateSurveySettingsAdmin(admin.ModelAdmin):
    inlines = [InlineReceiptParamsAdmin]

    def save_related(self, request, form, formsets, change):
        super(AutomateSurveySettingsAdmin, self)\
            .save_related(request, form, formsets, change)

        FillOutKfcSurveyForms().delay()


admin.site.register(AutomateSurveySettings, AutomateSurveySettingsAdmin)