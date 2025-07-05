from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials
account_sid = 'ACc37fcb1833afd118a95902163948ccdf' # Enter your Account SID here from Twilio
auth_token= '569fc603db3d163f1c3650f2f84b010d' # Enter your Auth Token here from Twilio

client = Client(account_sid, auth_token)


# design send massage function
def send_whatsapp_message(recipient_number, message_body):
    try:
        massage = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
            
        )
        print(f"Message sent successfully!! Message SID: {massage.sid}")
    except Exception as e:
        print('An error occurred ')

# user input 
name =input("Enter recipient name: ")
recipient_number = input("Enter the recipient's WhatsApp number with country code (e.g., +1234567890): ")
message_body = input("Enter the message you want to send to {name}: ")


# parse time,date and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24 hr formate): ")

schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# calculate_delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds < 0:
    print("The scheduled time is in the past. Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent in {name} at {schedule_datetime}.")

    # wait until the scheduled time
    time.sleep(delay_seconds) 


    # send the message
    send_whatsapp_message(recipient_number, message_body)