from twilio.rest import Client
import os
import datetime

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM")
TO_NUMBER = os.getenv("TWILIO_TO")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Get today's day
today = datetime.datetime.now().strftime("%A")

# Different messages for different days
messages = {
    "Monday": "🌞 Happy Monday! Don’t forget to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay ❤️",
    "Tuesday": "💪 Tuesday reminder! You got to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay  😘",
    "Wednesday": "🌼 Midweek reminder: stay awesome and Don’t forget to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay❤️",
    "Thursday": "🔥 Thursday nudge! Don’t forget to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay ❤️😊",
    "Friday": "🎉 Friday reminder — almost weekend and stay awesome and Don’t forget to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay❤️❤️",
    "Saturday": "☀️ Weekend reminder! Stay happy and stay awesome and Don’t forget to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay❤️ 😘",
    "Sunday": "🌸 Sunday gentle reminder ❤️ Rest well and stay awesome and Don’t forget to take your Malt and medicine😊 Love you a lot❤️ Message from your Jay❤️"
}

MESSAGE = messages.get(today, "❤️ Daily reminder for your task!")

msg = client.messages.create(
    body=MESSAGE,
    from_=FROM_NUMBER,
    to=TO_NUMBER
)

print(f"Message sent for {today}")