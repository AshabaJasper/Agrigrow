# works with both python 2 and 3
from __future__ import print_function

import africastalking

class VOICE:
    def __init__(self):
		# Set your app credentials
        self.username = "sandbox"
        self.api_key = "691a6d69eedb678a440be20b1ead894c9a00f3b494fb533b1ea5e70fad26d357"
		# Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
		# Get the voice service
        self.voice = africastalking.Voice

    def call(self):
        # Set your Africa's Talking phone number in international format
        callFrom = "+256783420287"
        # Set the numbers you want to call to in a comma-separated list
        callTo   = ["+256788336339"]
        try:
			# Make the call
            result = self.voice.call(callFrom, callTo)
            print (result)
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))

if __name__ == '__main__':
    VOICE().call()