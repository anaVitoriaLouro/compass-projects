from twilio.rest import Client
import os

def send_message(text, from_number):
    
    #Dados da conta Twilio
    account_sid = os.environ['ACCOUNT_SID']
    auth_token  = os.environ['AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to = str(from_number),
        from_ = "whatsapp:+14155238886",
        body=text)
    
    print('message', message)
    return message
