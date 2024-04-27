import africastalking

username = 'agrigrow'  # Use 'sandbox' for testing in the sandbox environment
api_key = '7c9ab98ce65e7741e424b7f07d7cd3c4404811732220fed5ac860573333c2ba2'

 
# Initialize SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS



import ssl
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

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

# Make a request to the Africa's Talking API
try:
    response = session.post(
        'https://api.africastalking.com/version1/messaging',
        headers={'apiKey': api_key, 'Content-Type': 'application/x-www-form-urlencoded'},
        data={'username': username, 'to': '+256788336339', 'message': 'Hello from Agrigrow!'}, verify=False
    )
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f'Encountered an error while sending SMS: {e}')
