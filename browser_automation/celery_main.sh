#!/bin/bash
# -A appname -Q queuename
celery -A browser_automation -Q main worker -l info