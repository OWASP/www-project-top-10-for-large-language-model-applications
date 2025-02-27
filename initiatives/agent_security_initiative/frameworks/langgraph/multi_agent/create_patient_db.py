"""
Script generated using gpt-4o. Prompt: "Generate a sqlite file with fake data about ALS patients"

Context on some of the medical related columns:
ALSFRS-R Score: Is a clinical tool to measure disease progression in ALS patients. It ranges from 0 (severe disability) to 48 (normal function).
FVC Percentage: Refers to the Forced Vital Capacity percentage, showing varying lung capacities.
Bulbar-Onset Flag: Indicates if the ALS onset is bulbar (1) or limb (0).
"""
import sqlite3
import random
import faker

# Initialize Faker library
fake = faker.Faker()

# Create a connection to a new SQLite database (als_patients.db)
conn = sqlite3.connect('als_patients.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS patients")

# Create the patients table
cursor.execute('''CREATE TABLE patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    gender TEXT,
                    diagnosis_date TEXT,
                    alsfrs_r_score INTEGER,
                    fvc_percentage REAL,
                    is_bulbar_onset INTEGER
                )''')


# Function to generate a fake ALS patient record
def generate_fake_patient():
    name = fake.name()
    age = random.randint(30, 80)  # ALS mainly affects people between these ages
    gender = random.choice(['Male', 'Female'])
    diagnosis_date = fake.date_between(start_date='-5y', end_date='today')
    alsfrs_r_score = random.randint(0, 48)  # typical range for ALSFRS-R scale
    fvc_percentage = round(random.uniform(25.0, 100.0), 2)  # Forced Vital Capacity percentage
    is_bulbar_onset = random.choice([0, 1])  # 0: limb-onset, 1: bulbar-onset

    return (name, age, gender, diagnosis_date, alsfrs_r_score, fvc_percentage, is_bulbar_onset)


# Insert fake data into the patients table
for _ in range(100):  # Generating 100 fake patient records
    patient = generate_fake_patient()
    cursor.execute('''INSERT INTO patients (name, age, gender, diagnosis_date, alsfrs_r_score, fvc_percentage, is_bulbar_onset)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', patient)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database als_patients.db created with fake data.")