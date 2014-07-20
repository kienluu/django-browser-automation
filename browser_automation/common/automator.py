from selenium.webdriver import Chrome, ChromeOptions

import logging
from selenium.webdriver.support.select import Select

LOG = logging.getLogger(__name__)


# noinspection PyAttributeOutsideInit
class AutomatorMixin(object):
    class UnexpectedSituation(Exception):
        pass

    data_property_class = None

    def __init__(self, steps, data_args=[]):
        self.steps = steps
        self.data = self.data_property_class(*data_args)

    def run(self):
        options = ChromeOptions()
        options.add_argument('--test-type')
        self.driver = Chrome(chrome_options=options)
        self.perform_steps()
        self.driver.close()

    def find_element(self, selector):
        LOG.info('finding selector "%s"' % selector)
        return self.driver.find_element_by_css_selector(selector)

    @property
    def action_method_lookup(self):
        return self.get_action_method__lookup()

    def get_action_method__lookup(self):
        return {
            'click': self.perform_click,
            'fill_form': self.perform_fill_form,
            'select_drop_down': self.perform_select_drop_down,
        }

    def get_css_selector(self, action):
        return action.get('css_selector')

    def get_action_value(self, action):
        if 'value' in action:
            value = action['value']
        elif 'property' in action:
            property_name = action['property']
            value = getattr(self.data, property_name)
        else:
            raise AutomatorMixin.UnexpectedSituation('Cannot find key "property" or "value"')

        return value

    def perform_steps(self):
        for step in self.steps:
            if 'url' in step:
                self.driver.get(step['url'])
            if 'actions' in step:
                self.perform_actions(step['actions'])

    def perform_actions(self, actions):
        for action in actions:
            action_method = self.action_method_lookup[action['type']]
            action_method(action)

    def perform_click(self, action):
        selector = self.get_css_selector(action)
        if selector:
            self.find_element(selector).click()
            return

        # Find by id.  This will be needed when people use "." in their id names.  Such as kfc's survey
        css_id = action['id_selector']
        LOG.info(css_id)
        self.driver.find_element_by_id(css_id).click()

    def perform_fill_form(self, action):
        selector = self.get_css_selector(action)
        value = self.get_action_value(action)

        self.find_element(selector).send_keys(value)

    def perform_select_drop_down(self, action):
        selector = self.get_css_selector(action)
        value = self.get_action_value(action)

        Select(self.find_element(selector)).select_by_value(value)
