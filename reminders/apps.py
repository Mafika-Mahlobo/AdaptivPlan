"""
A threaded task to run 'send_reminders' management command at regular intervals (3 min)
"""

from django.apps import AppConfig
import threading
import time
from django.core.management import call_command
import sys


class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'

    def ready(self):
        if any(cmd in sys.argv for cmd in ["runserver", "gunicorn", "uwsqi"]):
            def schedule_reminders():
                while True:
                    call_command("send_reminders")
                    time.sleep(300)
        
            thread = threading.Thread(target=schedule_reminders, daemon=True)
            thread.start()

