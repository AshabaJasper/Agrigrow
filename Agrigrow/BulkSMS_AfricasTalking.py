import africastalking
import tkinter as tk
from tkinter import messagebox

# Initialize Africa's Talking API
username = 'agrigrow'  # Use 'sandbox' for testing in the sandbox environment
api_key = '7c9ab98ce65e7741e424b7f07d7cd3c4404811732220fed5ac860573333c2ba2'
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Function to send SMS
def send_sms(recipient, message):
    try:
        response = sms.send(message, [recipient])
        if response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
            messagebox.showinfo("Success", "SMS sent successfully!")
        else:
            error_message = response['SMSMessageData']['Recipients'][0]['status']
            messagebox.showerror("Error", f"Failed to send SMS: {error_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Encountered an error while sending SMS: {str(e)}")

# GUI setup
def on_send():
    recipient = recipient_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    if recipient and message:
        send_sms(recipient, message)
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
