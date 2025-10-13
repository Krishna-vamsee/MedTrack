# display.py
import database as db
import notifier as nt
import os

# ----------------- Sample Medicines -----------------
sample_medicines = [
    {"name": "Multivitamin", "dosage": "500mg", "time": "06:30"},
    {"name": "Aspirin", "dosage": "75mg", "time": "07:00"},
    {"name": "Metformin", "dosage": "500mg", "time": "08:00"},
    {"name": "Dolo", "dosage": "3mg", "time": "8:300"},
    {"name": "Vitamin D", "dosage": "1000 IU", "time": "12:00"},
    {"name": "Fish Oil", "dosage": "1000mg", "time": "13:00"},
    {"name": "Calcium", "dosage": "500mg", "time": "17:00"},
    {"name": "Metformin", "dosage": "500mg", "time": "18:00"},
    {"name": "Probiotic", "dosage": "10 billion CFU", "time": "20:00"},
    {"name": "Melatonin", "dosage": "3mg", "time": "21:00"}
]

# ----------------- Menu -----------------
def show_menu():
    print("\n--- MedTrack Menu ---")
    print("1) Add Medicine")
    print("2) View Medicines")
    print("3) Delete Medicine")
    print("4) Mark Medicine as Taken")
    print("5) Start Reminder Service")
    print("6) Clear All Medicines")
    print("7) Delete Database File")
    print("8) Restart Database (Drop & Recreate Table)")
    print("9) Add Sample Medicines")
    print("10) Exit")

# ----------------- Summary Function -----------------
def view_summary():
    meds = db.view_medicines()
    total = len(meds)
    taken = sum(1 for m in meds if m[4] == 'Taken')
    pending = total - taken
    return {"total": total, "taken": taken, "pending": pending}

# ----------------- Main Function -----------------
def main(print_footer):
    db.init_db()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Medicine Name: ").strip()
            dosage = input("Dosage (e.g., 500mg): ").strip()
            at_time = input("Time (HH:MM 24h format): ").strip()
            if db.add_medicine(name, dosage, at_time):
                print_footer(f"Added {name} at {at_time}")

        elif choice == "2":
            meds = db.view_medicines()
            if meds:
                print("\n--- Scheduled Medicines ---")
                for mid, name, dosage, at_time, status in meds:
                    print(f"ID: {mid} | {name} | {dosage} | {at_time} | {status}")
                print_footer("End of list")
            else:
                print_footer("No medicines scheduled yet")

        elif choice == "3":
            try:
                mid = int(input("Enter ID to delete: ").strip())
                db.delete_medicine(mid)
                print_footer(f"Deleted medicine ID {mid}")
            except ValueError:
                print_footer("Invalid numeric ID")

        elif choice == "4":
            try:
                mid = int(input("Enter ID to mark Taken: ").strip())
                db.mark_taken(mid)
                print_footer(f"Marked ID {mid} as Taken")
            except ValueError:
                print_footer("Invalid numeric ID")

        elif choice == "5":
            print_footer("Starting reminder service. Keep this window open.")
            nt.schedule_reminders()

        elif choice == "6":
            confirm = input("Clear all medicines? (y/n): ").strip().lower()
            if confirm == 'y':
                db.clear_all_medicines()
                print_footer("All medicine records cleared")
            else:
                print_footer("Operation canceled")

        elif choice == "7":
            confirm = input("Delete the database file? (y/n): ").strip().lower()
            if confirm == 'y':
                db_path = "data/medicines.db"
                if os.path.exists(db_path):
                    os.remove(db_path)
                    print_footer("Database file deleted. A new one will be created automatically.")
                else:
                    print_footer("Database file not found")
            else:
                print_footer("Operation canceled")

        elif choice == "8":
            confirm = input("Restart database (drop & recreate table)? (y/n): ").strip().lower()
            if confirm == 'y':
                db.reset_database()
                print_footer("Database reset successfully")
            else:
                print_footer("Operation canceled")

        elif choice == "9":
            confirm = input("Add sample medicines to the database? (y/n): ").strip().lower()
            if confirm == "y":
                db.init_db()  # Ensure table exists
                for med in sample_medicines:
                    db.add_medicine(med["name"], med["dosage"], med["time"])
                print_footer("Sample medicines added successfully")
            else:
                print_footer("Operation canceled")

        elif choice == "10":
            print_footer("Thank you for using MedTrack.\nRemember: Take your medicines on time and stay healthy.")
            break

        else:
            print_footer("Invalid choice. Try again")
