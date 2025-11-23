from twilio.rest import Client
import os

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM")
TO_NUMBER = os.getenv("TWILIO_TO")

MESSAGE = "Good morning My love❤️ Just a reminder to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

msg = client.messages.create(
    body=MESSAGE,
    from_=FROM_NUMBER,
    to=TO_NUMBER
)

print("Message sent successfully!")