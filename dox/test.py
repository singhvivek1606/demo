
from faker import Faker
import csv
import random
from datetime import datetime

# Initialize Faker for Indian data
fake = Faker("en_IN")

# Sample hobbies, professions, and education
hobbies = [
    "Reading", "Cricket", "Football", "Traveling",
    "Cooking", "Photography", "Gaming", "Music",
    "Dancing", "Painting", "Gardening", "Swimming"
]

professions = [
    "Software Engineer", "Data Analyst", "Doctor",
    "Teacher", "Business Analyst", "Accountant",
    "Lawyer", "Civil Engineer", "Marketing Manager",
    "Data Scientist", "Entrepreneur", "Nurse",
    "Graphic Designer", "Professor"
]

education_levels = [
    "High School", "Diploma", "B.Tech", "B.Sc",
    "B.Com", "BBA", "BCA", "M.Tech", "M.Sc",
    "MBA", "MCA", "MBBS", "PhD"
]


def generate_fake_data(num_records):
    filename = f"fake_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    columns = [
        "ID", "Name", "Gender", "Age",
        "Email", "Mobile Number", "Address",
        "City", "State", "Pincode",
        "Hobby", "Profession", "Education",
        "Company", "Date of Birth"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        for i in range(1, num_records + 1):
            gender = random.choice(["Male", "Female"])

            if gender == "Male":
                name = fake.name_male()
            else:
                name = fake.name_female()

            date_of_birth = fake.date_of_birth(
                minimum_age=18,
                maximum_age=65
            )

            age = (
                datetime.today().date() - date_of_birth
            ).days // 365

            record = {
                "ID": i,
                "Name": name,
                "Gender": gender,
                "Age": age,
                "Email": fake.email(),
                "Mobile Number": fake.numerify("##########"),
                "Address": fake.street_address(),
                "City": fake.city(),
                "State": fake.state(),
                "Pincode": fake.postcode(),
                "Hobby": random.choice(hobbies),
                "Profession": random.choice(professions),
                "Education": random.choice(education_levels),
                "Company": fake.company(),
                "Date of Birth": date_of_birth
            }

            writer.writerow(record)

    print(f"\nSuccessfully generated {num_records} records!")
    print(f"CSV File: {filename}")


if __name__ == "__main__":
    try:
        num_records = int(input("How many records do you want to generate? "))

        if num_records <= 0:
            print("Please enter a positive number.")
        else:
            generate_fake_data(num_records)

    except ValueError:
        print("Invalid input! Please enter a valid number.")
