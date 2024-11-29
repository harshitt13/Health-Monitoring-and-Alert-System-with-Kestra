import json
import random

#random data generation
patient_data = {
    "heart_rate":random.randint(70, 120, 1000),
    "glucose_level":random.randint(60, 120, 1000)
}

#write data to json file
with open('patient_data.json', 'w') as json_file:
    json.dump(patient_data, json_file)

print("Data written to json file")