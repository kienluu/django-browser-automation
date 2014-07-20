from celery import Task
from kfc_survey.automator import KfcSurveyAutomator
from kfc_survey.models import AutomateSurveySettings
from kfc_survey.utils.responses import get_responses


class FillOutKfcSurveyForm(Task):

    def run(self, automate_survey_settings_id):
        survey_settings = AutomateSurveySettings.objects.get(id=automate_survey_settings_id)

        answers = get_responses(survey_settings.type)

        receipt = survey_settings.receiptparams

        automator = KfcSurveyAutomator(answers, receipt=receipt, data_args=[receipt])

        automator.run()

        return
