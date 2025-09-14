from twilio.rest import Client
from datetime import datetime, timedelta
import time
#account_sid = 'ACad6806e98212fe46c871f9bd8d4d4bf8'
#auth_token = 'abfc461e667a18eb15041883fd7bf53b'
client = Client(account_sid, auth_token)
def send_whatsapp_message(message_body, recipient_number):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  
            body=message_body,
            to=f'whatsapp:{recipient_number}'  # use user input
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")
name = input('Enter the recipient name=')
recipient_number = input('Enter the recipient Whatsapp number with country code(e.d, +12345):')
message_body = input(f'enter the message you want to send to{name}:')
date_str = input("Enter the date to send the message (YYYY-MM-DD):")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format):")

#datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime 
delay_seconds = time_difference.total_seconds()
if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time:')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}')

    time.sleep(delay_seconds)
    send_whatsapp_message(message_body, recipient_number)

