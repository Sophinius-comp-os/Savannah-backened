"""
UTILITY file for sending sms
"""


import africastalking
import phonenumbers
from decouple import config


# Initialize the SDK
def initialize_sdk():
    africastalking.initialize(
        username=config('AT_USERNAME'), 
        api_key=config('AT_APIKEY')
    )

def format_phone_number(phone):
    try:
        parsed_number = phonenumbers.parse(phone, "KE")
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            raise ValueError(f"Invalid phone number: {phone}")
    except phonenumbers.NumberParseException as e:
        raise ValueError(f"Number parsing error: {e}")

def send_sms(to, message):
    initialize_sdk()
    formatted_phone = format_phone_number(to)
    sms = africastalking.SMS
    response = sms.send(message, [formatted_phone])
    return response

