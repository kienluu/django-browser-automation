from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "run kfc survey"

    def handle(self, *args, **options):
        from kfc_survey.tasks import FillOutKfcSurveyForm
        FillOutKfcSurveyForm().run(1)