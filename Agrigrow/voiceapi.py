from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/queryBalance', methods=['POST'])
def query_balance():
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')

    if is_active == '1':
        # Compose the XML response when the call is active
        response = '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <GetDigits timeout="30" finishOnKey="#">
        <Say voice="woman">Please enter your account number followed by the hash sign</Say>
    </GetDigits>
</Response>'''

        # Set the response content type and return the response
        return make_response(response, 200, {'Content-Type': 'text/plain'})

    return 'Call is not active', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
