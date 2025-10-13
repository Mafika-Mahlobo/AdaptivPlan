"""
A custom management command to send reminder emails.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from zoneinfo import ZoneInfo
from tasks.models import Task
from django.core.cache import cache

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        handle method override iterate through tasks to send reminders based on the day of the week
        , tasks start time, and current time (users chosen timezone)
        """

        now_utc = timezone.now()

        assigned_tasks = Task.objects.exclude(slot=None).select_related("slot", "user")
        total_checked = 0
        total_sent = 0

        for task in assigned_tasks:

            slot = task.slot
            user = task.user

            local_zone = ZoneInfo(getattr(user, "time_zone", "Africa/Johannesburg"))
            now = timezone.localtime(now_utc, local_zone)
            today = now.isoweekday()
            upcoming = now + timedelta(minutes=10)

            total_checked += 1
            cache_key = f"reminder_sent_task_{task.id}"
            
            week_days = []
            for d in slot.week_days:
                try:
                    week_days.append(int(d))
                except (TypeError, ValueError):
                    pass

            if today not in week_days:
                self.stdout.write(self.style.WARNING("Skipped (not scheduled for today)"))
                continue

            slot_start = timezone.make_aware(
                timezone.datetime.combine(now.date(), slot.start_time),
                local_zone
            )

            
            if now <= slot_start <= upcoming:
                total_sent += 1
                self.stdout.write(f"Sending reminder for {slot.name} ({slot.start_time})")

                if not cache.get(cache_key):
                    send_mail(
                        subject="Your task in starting soon!",
                        message=f"Hi {user.first_name},\n\n You task '{task.title}' starts at {slot.start_time}.",
                        from_email="AdaptivPlan.co.za",
                        recipient_list=[slot.user.email],
                        fail_silently=False,
                    )
                    cache.set(cache_key, True, timeout=1800)
            else:
                self.stdout.write(self.style.WARNING("Not in 10-minute window"))

        self.stdout.write(self.style.SUCCESS(f"\nSummary: Checked {total_checked} slots, sent {total_sent} reminders."))