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
    kestra_endpoint = "{{ kestra_endpoint }}"  # Replace with your Kestra API endpoint
    workflow_id = "{{ workflow_id }}"  # Replace with your workflow ID
    namespace = "{{ namespace }}"  # Replace with your namespace

    payload = {
        "namespace": namespace,
        "flowId": workflow_id,
        "inputs": {
            "heart_rate": str(heart_rate),  # Ensure it's a string
            "glucose_level": str(glucose_level)  # Ensure it's a string
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

"""
# Example usage
trigger_kestra_workflow(heart_rate=190, glucose_level=400)
"""