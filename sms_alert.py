from twilio.rest import Client

def send_sms_alert(heart_rate, glucose_level):
    # Send an SMS alert for critical levels.
    # Replace with your Twilio credentials
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    twilio_number = "+1234567890"
    recipient_number = "+0987654321"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Critical Alert! Heart Rate: {heart_rate} bpm, Glucose Level: {glucose_level} mg/dL.",
        from_=twilio_number,
        to=recipient_number
    )
    print("Alert sent:", message.sid)
