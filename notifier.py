# notifier.py
import schedule
import time
from datetime import datetime

try:
    from plyer import notification
    HAS_NOTIFIER = True
except ImportError:
    HAS_NOTIFIER = False

import database as db

def send_notification(title, message):
    if HAS_NOTIFIER:
        try:
            notification.notify(title=title, message=message, timeout=10)
        except Exception as e:
            print(f"[Notification Error] {title}: {message} [{e}]")
    else:
        print(f"[NOTIFY] {title} - {message}")

def _notify_due(name, dosage):
    msg = f"It's time to take: {name} ({dosage})"
    send_notification("MedTrack Reminder", msg)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}")

def schedule_reminders():
    meds = db.view_medicines()
    if not meds:
        print("No medicines scheduled. Add some first.")
        return

    schedule.clear()
    for mid, name, dosage, at_time, status in meds:
        try:
            schedule.every().day.at(at_time).do(_notify_due, name=name, dosage=dosage)
        except Exception:
            print(f"Skipping invalid time '{at_time}' for {name}")

    schedule.every().day.at("00:00").do(db.reset_statuses)

    print("Reminder service is running. Keep this window open.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReminder service stopped.")
