import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler

# Load simulated patient data
with open('patient_data.json', 'r') as f:
    patient_data = json.load(f)

# Combine heart rate and glucose data into a matrix
data = np.column_stack((patient_data["heart_rate"], patient_data["glucose_level"]))

# Scale the data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Save preprocessed data
np.save('preprocessed_data.npy', scaled_data)
print("Preprocessed data saved:", scaled_data)
