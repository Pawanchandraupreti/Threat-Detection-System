import requests
import json

SLACK_WEBHOOK = "https://hooks.slack.com/services/XXXXX"

def send_slack_alert(ip, message):
    payload = {
        "text": f"🚨 THREAT DETECTED 🚨",
        "attachments": [{
            "text": f"IP: {ip}\nMessage: {message}",
            "color": "#ff0000"
        }]
    }
    requests.post(SLACK_WEBHOOK, json=payload)

# Example usage
send_slack_alert("192.168.1.100", "Brute-force attack detected!")
