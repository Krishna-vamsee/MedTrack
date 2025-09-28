import database as db

sample_medicines = [
    {"name": "Multivitamin", "dosage": "500mg", "time": "06:30"},
    {"name": "Aspirin", "dosage": "75mg", "time": "07:00"},
    {"name": "Metformin", "dosage": "500mg", "time": "08:00"},
    {"name": "Vitamin D", "dosage": "1000 IU", "time": "12:00"},
    {"name": "Fish Oil", "dosage": "1000mg", "time": "13:00"},
    {"name": "Calcium", "dosage": "500mg", "time": "17:00"},
    {"name": "Metformin", "dosage": "500mg", "time": "18:00"},
    {"name": "Probiotic", "dosage": "10 billion CFU", "time": "20:00"},
    {"name": "Melatonin", "dosage": "3mg", "time": "21:00"}
]

# Initialize DB and add sample medicines
db.init_db()
for med in sample_medicines:
    db.add_medicine(med["name"], med["dosage"], med["time"])

print("Sample medicines added to the database.")
