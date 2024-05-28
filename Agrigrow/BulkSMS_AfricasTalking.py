import africastalking
import ssl
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import tkinter as tk
from tkinter import messagebox
import certifi

# Africa's Talking API credentials
username = 'agrigrow'  # Use 'sandbox' for testing in the sandbox environment
api_key = '7c9ab98ce65e7741e424b7f07d7cd3c4404811732220fed5ac860573333c2ba2'

# Initialize SDK
africastalking.initialize(username, api_key)

# SSL Adapter class for handling SSL/TLS versions
class SSLAdapter(HTTPAdapter):
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version
        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=self.ssl_version,
        )

# Instantiate the adapter with the desired SSL version
adapter = SSLAdapter(ssl_version=ssl.PROTOCOL_TLSv1_2)

# Create a session and mount the adapter
session = requests.Session()
session.mount('https://', adapter)

# Function to send SMS
def send_sms(recipient, message):
    try:
        response = session.post(
            'https://api.africastalking.com/version1/messaging',
            headers={'apiKey': api_key, 'Content-Type': 'application/x-www-form-urlencoded'},
            data={'username': username, 'to': recipient, 'message': message},
            verify=certifi.where()  # Verify using certifi
        )
        response_json = response.json()
        if response.status_code == 201:
            messagebox.showinfo("Success", "SMS sent successfully!")
        else:
            messagebox.showerror("Error", f"Failed to send SMS: {response_json}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Encountered an error while sending SMS: {e}")

# GUI setup
def on_send():
    recipient = recipient_entry.get()
    message = message_entry.get("1.0", tk.END)
    if recipient and message.strip():
        send_sms(recipient, message.strip())
    else:
        messagebox.showwarning("Input Error", "Please provide both recipient and message.")

root = tk.Tk()
root.title("Send SMS")

tk.Label(root, text="Recipient Phone Number").grid(row=0, column=0, padx=10, pady=10)
recipient_entry = tk.Entry(root, width=30)
recipient_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Message").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Text(root, width=40, height=10)
message_entry.grid(row=1, column=1, padx=10, pady=10)

send_button = tk.Button(root, text="Send SMS", command=on_send)
send_button.grid(row=2, columnspan=2, pady=20)

root.mainloop()
