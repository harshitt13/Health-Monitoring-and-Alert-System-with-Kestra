from data_processing import generate_mock_data
from randomforest import train_model, load_model, predict_critical_levels
from sms_alert import send_sms_alert
import requests

"""""
# Only run this once or when retraining is needed.

# Generate mock data
data = generate_mock_data()

# Train the model
train_model(data)

# Load the trained model
model = load_model()
"""

# Trigger Kestra workflow
def trigger_kestra_workflow(heart_rate, glucose_level):
    kestra_endpoint = "http://localhost:8080/api/v1/executions"
    workflow_id = "health-alerts"
    namespace = "health.monitoring"

    payload = {
        "namespace": namespace,
        "flowId": workflow_id,
        "inputs": {
            "heart_rate": heart_rate,
            "glucose_level": glucose_level
        }
    }

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(kestra_endpoint, json=payload, headers=headers)
        if response.status_code == 200:
            print("Workflow triggered successfully:", response.json())
        else:
            print("Failed to trigger workflow:", response.status_code, response.text)
    except Exception as e:
        print("Error triggering Kestra workflow:", str(e))

# Example usage
trigger_kestra_workflow(heart_rate=190, glucose_level=400)