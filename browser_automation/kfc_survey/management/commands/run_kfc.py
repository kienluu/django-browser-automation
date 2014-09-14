from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "run kfc surveys"

    def handle(self, *args, **options):
        from kfc_survey.tasks import FillOutKfcSurveyForms
        FillOutKfcSurveyForms().run()