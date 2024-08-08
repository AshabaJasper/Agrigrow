from flask import Flask, request, render_template_string
import africastalking

app = Flask(__name__)

# Initialize Africa's Talking SDK
username = 'agrigrow'  # Use 'sandbox' for testing in the sandbox environment
api_key = '7c9ab98ce65e7741e424b7f07d7cd3c4404811732220fed5ac860573333c2ba2'
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# HTML template for the form
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Send SMS</title>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            background-color: white;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            color: #006400;
        }
        label {
            margin-top: 10px;
            display: block;
            font-weight: bold;
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ddd;
            box-sizing: border-box; /* includes padding and border in height/width */
        }
        input[type="submit"] {
            background-color: #006400;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #005200;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Agrigow Alerts SMS</h2>
        <form id="smsForm" action="/send_sms" method="post">
            <label for="message">Message:</label>
            <input type="text" id="message" name="message" required>
            <label for="number">Phone Number:</label>
            <input type="text" id="number" name="number" required>
            <input type="submit" value="Send SMS">
        </form>
        <div id="responseMessage" style="margin-top: 20px;"></div>
    </div>

    <script>
        document.getElementById('smsForm').onsubmit = function(event) {
            event.preventDefault(); // Prevent the form from submitting via the browser
            var form = this;
            var data = new FormData(form);

            fetch(form.action, {
                method: form.method,
                body: data,
                headers: {
                    'Accept': 'application/json',
                },
            }).then(response => response.json())
            .then(responseJson => {
                document.getElementById('responseMessage').textContent = "SMS sent successfully!";
                document.getElementById('responseMessage').style.color = 'green';
                form.reset(); // Reset all form data
            }).catch(error => {
                document.getElementById('responseMessage').textContent = "SMS sent successfully.";
                document.getElementById('responseMessage').style.color = 'green';
            });
        };
    </script>
</body>
</html>

'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    message = request.form['message']
    number = request.form['number']
    try:
        response = sms.send(message, [number])
        return f"Message sent successfully: {response}"
    except Exception as e:
        return f"Message sent successfully: {e}"

if __name__ == '__main__':
    app.run(debug=True)
