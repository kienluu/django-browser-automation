from common.automator import AutomatorMixin


class KfcSurveyAutomator(AutomatorMixin):
    class DataProperty(object):
        def __init__(self, receipt):
            self.receipt = receipt

        @property
        def store_number(self):
            return self.receipt.store_number

        @property
        def order_number(self):
            return self.receipt.order_number

        @property
        def order_year(self):
            return str(self.receipt.order_datetime.year)

        @property
        def order_month(self):
            return '%02d' % self.receipt.order_datetime.month

        @property
        def order_day(self):
            return '%02d' % self.receipt.order_datetime.day

        @property
        def order_hour(self):
            return self.receipt.order_datetime.strftime('%I')

        @property
        def order_minute(self):
            return '%02d' % self.receipt.order_datetime.minute

        @property
        def order_meridian(self):
            return self.receipt.order_datetime.strftime('%p').upper()

    data_property_class = DataProperty

    def __init__(self, *args, **kwargs):
        self.receipt = kwargs.pop('receipt')
        super(KfcSurveyAutomator, self).__init__(*args, **kwargs)

    def get_action_method__lookup(self):
        lookup = super(KfcSurveyAutomator, self).get_action_method__lookup()
        lookup.update({"save_validation_code": self.perform_save_validation_code})
        return lookup

    def perform_save_validation_code(self, action):
        selector = self.get_css_selector(action)
        try:
            validation_code = self.find_element(selector).text
        except Exception as e:
            # TODO: save screen shot and store in media directory and model
            # self.driver.get_screenshot_as_file()
            raise e
        self.receipt.validation_code = validation_code
        self.receipt.save()

