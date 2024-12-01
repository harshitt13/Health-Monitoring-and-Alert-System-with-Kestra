from data_processing import generate_mock_data
from randomforest import train_model, load_model, predict_critical_levels
from sms_alert import send_sms_alert

# Step 1: Generate mock data
data = generate_mock_data()

# Step 2: Train the model (only run this once or when retraining is needed)
train_model(data)

# Step 3: Load the trained model
model = load_model()

# Step 4: Simulate real-time monitoring
for index, row in data.iterrows():
    heart_rate = row['heart_rate']
    glucose_level = row['glucose_level']
    
    is_critical = predict_critical_levels(model, heart_rate, glucose_level)
    if is_critical:
        send_sms_alert(heart_rate, glucose_level)
