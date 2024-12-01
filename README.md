<div align="center">

# Health Monitoring and Alert System with Kestra

![GitHub last commit](https://img.shields.io/github/last-commit/harshitt13/Smart_Health_Care_Automated_System)
![GitHub repo size](https://img.shields.io/github/repo-size/harshitt13/Smart_Health_Care_Automated_System)
![GitHub stars](https://img.shields.io/github/stars/harshitt13/Smart_Health_Care_Automated_System)

This project uses Kestra to monitor health data such as heart rate and glucose levels. When critical levels are detected, an SMS alert is sent using Twilio's messaging API.

</div>

## Overview

- **Kestra** is an open-source orchestration platform for workflows and data pipelines.
- This workflow monitors heart rate and glucose levels from input data and sends critical alerts via SMS using **Twilio** when the values exceed defined thresholds.
  
## Features

- Accepts `heart_rate` and `glucose_level` as input.
- Checks if the values exceed critical thresholds.
- Sends an alert via Twilio SMS if critical levels are detected.
  
## Prerequisites

Before running the workflow, make sure the following are set up:

1. **Kestra**: Ensure Kestra is installed and running on your system. If you're new to Kestra, refer to the [official documentation](https://kestra.io) to get started.
2. **Twilio Account**: Create a Twilio account and get your Account SID, Auth Token, and a Twilio phone number. For more information on how to set up Twilio, refer to [Twilio's official guide](https://www.twilio.com/docs/usage/keys-and-sid).
3. **Kestra Plugin for HTTP**: Make sure that the Kestra HTTP plugin is installed and configured. If it is not installed, follow the steps in the Kestra documentation to install it.

## Setting Up

### 1. Install Kestra
Follow the installation guide on [Kestra's website](https://kestra.io/docs/installation) to install and run Kestra on your local machine or server.

### 2. Install the HTTP Plugin (If Not Already Installed)
The HTTP plugin is required to send HTTP requests (used for Twilio integration). Ensure this plugin is enabled in your Kestra setup. If it's missing, consult the [Kestra Plugin documentation](https://kestra.io/plugins).

### 3. Configure Your Twilio API Credentials
In your Kestra YAML configuration file, replace the placeholders with your Twilio Account SID, Auth Token, and Twilio phone number:

- `twilio_account_sid`: Your Twilio Account SID
- `YourTwilioAuthToken`: Your Twilio Auth Token
- `your_twilio_phone_number`: The phone number you got from Twilio
- `recipient_phone_number`: The phone number to which the SMS alert will be sent.

### 4. Define the Workflow

Create a `.yml` file (e.g., `health-monitoring.yml`) with the configuration from health_alert.yml
