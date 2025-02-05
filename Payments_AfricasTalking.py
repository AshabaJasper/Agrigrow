import africastalking
username = 'sandbox'  # Use 'sandbox' for testing in the sandbox environment
api_key = 'ad1981292e6a13b51f38f220c908752b8aa7bb77ac0348652c137975770dd443'


# Initialize SDK
africastalking.initialize(username, api_key)

# Get the payment service
payments = africastalking.Payment

# Define payment parameters
product_name = 'AgrigrowProducts'
phone_number = '+256712345678'
currency_code = 'UGX'
amount = 5000.00
metadata = {'description': 'Payment for seeds'}

# Initiate the mobile checkout
try:
    response = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
    print(response)
except Exception as e:
    print(f'Error initiating payment: {e}')
