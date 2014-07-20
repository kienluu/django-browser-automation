#!/bin/bash
# -A appname -Q queuename
# default queue name can be set with CELERY_DEFAULT_QUEUE
celery -A browser_automation -Q default worker -l info
