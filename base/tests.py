# from django.test import TestCase

# Create your tests here.
from datetime import datetime

# Assuming you have the donor's DOB in the format 'YYYY-MM-DD'
dob_str = '1990-05-15'  # Replace this with the actual DOB

# Convert the DOB string to a datetime object
dob = datetime.strptime(dob_str, '%Y-%m-%d')

# Calculate the current date
current_date = datetime.now()

# Calculate the donor's age
age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

# Print the donor's age
print(f"The donor's age is {age} years.")
