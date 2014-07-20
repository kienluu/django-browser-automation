import json
import os

default_data_dir = os.path.join(os.path.dirname(__file__), '..', 'form_responses')


def get_responses(type):
    with open('%s/%s/data.json' % (default_data_dir, type)) as data_file:
        responses = json.loads(data_file.read())

    return responses