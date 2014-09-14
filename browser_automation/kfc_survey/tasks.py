from celery import Task
from django.db.models import Q
from kfc_survey.automator import KfcSurveyAutomator
from kfc_survey.models import AutomateSurveySettings
from kfc_survey.utils.responses import get_responses


class FillOutKfcSurveyForms(Task):

    def run(self, automate_survey_settings_id_list=None):
        if automate_survey_settings_id_list is None:
            survey_settings_list = AutomateSurveySettings.objects.filter(Q(receiptparams__validation_code='') | Q(receiptparams__validation_code__isnull=True))
        else:
            survey_settings_list = AutomateSurveySettings.objects.filter(id__in=automate_survey_settings_id_list)

        for survey_settings in survey_settings_list:
            answers = get_responses(survey_settings.type)
            receipt = survey_settings.receiptparams

            automator = KfcSurveyAutomator(answers, receipt=receipt, data_args=[receipt])
            automator.run()

        return
