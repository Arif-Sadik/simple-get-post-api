# test_client.py
import requests

BASE = "http://127.0.0.1:5000"  # your local server URL

def ping_server():
    """Test /ping endpoint"""
    try:
        r = requests.get(BASE + "/ping")
        print("PING response:", r.json())
    except Exception as e:
        print("Error pinging server:", e)

def post_message(text):
    """Send a message to /messages"""
    try:
        r = requests.post(BASE + "/messages", json={"text": text})
        print("POST response:", r.status_code, r.json())
    except Exception as e:
        print("Error posting message:", e)

def get_messages():
    """Retrieve all messages from /messages"""
    try:
        r = requests.get(BASE + "/messages")
        print("ALL messages:", r.json())
    except Exception as e:
        print("Error getting messages:", e)

if __name__ == "__main__":
    ping_server()
    post_message("Hello from Python client!")
    get_messages()
