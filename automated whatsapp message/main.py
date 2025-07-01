# By using twilio we can send real time messages to users on whatsapp or any social media apps without any manual effort

# step 1
from twilio.rest import Client
from datetime import datetime , timedelta
import time

# step-2 twilio credentials
account_sid ="AC272cd7e41036c8914c3f96552d2dd9fb";
account_token="67531cc60291b37ee864cd484ff585ad";

client= Client(account_sid, account_token)  # accound sid and token use to authanticate twilio api client () object use to create twilio client who can sned messages

# step-3 define send emssage function
def send_whatsapp_message(reciptant_number,message_body):
# step-3 define send emssage function
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_body,
            to=f"whatsapp:{reciptant_number}"
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")

 
 

# steo-4 user input
name = input("Enter the reciptent name: ")
reciptent_number= input("Enter the reciptent whatsapp number with country code (e.g, +12345): ")
message_body= input(f"Enter the message you want to send to {name}")

# step-5 parse datetime and calculate delay
date_str=input("Enter the date to send the message (YYYY-MM-DD): ")
time_str=input("Enter the time to send the message (HH:MM): ")

# Parse datetime
schedule_time = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_time = datetime.now()

# Calculate delay
time_difference = schedule_time - current_time
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time')
else:
    print(f"Message scheduled to be sent to {name} at {schedule_time}.")
    # Wait until the scheduled time
    time.sleep(delay_seconds)
    # Send the message
    send_whatsapp_message(reciptent_number, message_body)
