# MedTrack

**MedTrack** is a Python-based desktop application designed to help users manage their daily medications efficiently. It allows users to add, view, delete, and mark medicines as taken, and provides timely reminders through desktop notifications.

This project is ideal for anyone who wants to never miss a dose and keep track of their medicine schedule in a simple and intuitive way.

---

## Features

- Add, view, delete, and mark medicines as taken.
- Desktop notifications for timely reminders.
- Preload sample medicines for a full day schedule (morning to night).
- Database management:
  - Clear all medicine records (keep table).
  - Delete the database file entirely.
  - Restart the database (drop & recreate table).
- Simple, menu-driven interface.
- Data stored in SQLite for portability.


---
## Structure

MedTrack/
│
├── app.py            # Entry point
├── display.py        # User interface and menu
├── database.py       # Database operations
├── notifier.py       # Notifications and scheduling
├── requirements.txt  # Python dependencies
└── data/
    └── medicines.db  # SQLite database

---

