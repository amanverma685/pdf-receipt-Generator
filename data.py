import random
import string
from datetime import datetime, timedelta
def generate_random_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generateRandomDate():
    start_date = datetime(1900, 1, 1)
    end_date = datetime(2100, 12, 31)

    # Calculate the number of days between the start and end date
    date_range = (end_date - start_date).days

    # Generate a random number of days from the start date
    random_days = random.randint(0, date_range)

    # Create a random date by adding the random number of days to the start date
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")

def generate_random_contact():
    # Generate a random 10-digit phone number
    contact_number = "1"  # Start with the country code, e.g., +1 for the United States
    for _ in range(9):
        contact_number += str(random.randint(0, 9))

    return contact_number

def generate_random_gender():

    # List of possible gender labels
    genders = ["Male", "Female", "Non-binary", "Other", "Prefer not to say"]

    # Generate a random gender label
    random_gender = random.choice(genders)
    return random_gender



def generate_random_address():
    streets = ["123 Main Street", "456 Elm Avenue", "789 Oak Road", "321 Maple Lane", "555 Birch Boulevard"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    states = ["NY", "CA", "IL", "TX", "FL"]
    zip_codes = ["10001", "90001", "60601", "77001", "33101"]
    random_street = random.choice(streets)
    random_city = random.choice(cities)
    random_state = random.choice(states)
    random_zip = random.choice(zip_codes)

    random_address = f"{random_street}, {random_city}, {random_state} {random_zip}"
    
    return random_address

def generate_random_id(length=8, prefix=''):
    
    # Create a string of characters (letters and digits) to choose from
    characters = string.ascii_letters + string.digits
    
    # Generate the random part of the ID
    random_part = ''.join(random.choice(characters) for _ in range(length))
    
    # Combine the prefix and random part to form the ID
    generated_id = prefix + random_part
    
    return generated_id



def generate_random_medical_department():

    # List of possible medical department names
    medical_departments = [
        "Cardiology",
        "Orthopedics",
        "Pediatrics",
        "Dermatology",
        "Neurology",
        "Oncology",
        "Gastroenterology",
        "Obstetrics and Gynecology",
        "Psychiatry",
        "Radiology",
        "Urology",
        "Ophthalmology",
        "ENT (Ear, Nose, and Throat)",
        "Emergency Medicine",
    ]
    return random.choice(medical_departments)

