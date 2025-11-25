# 📲 WhatsApp Daily Reminder Bot (Twilio + GitHub Actions)

This project sends **automated daily WhatsApp reminder messages** using **Twilio WhatsApp API** and **GitHub Actions**.

The script runs fully in the cloud, so it works even if your phone or laptop is turned off.

---

## 🚀 Features

- ✅ Sends WhatsApp messages automatically
- ✅ Runs on a schedule using GitHub Actions
- ✅ No server needed
- ✅ Secure (uses GitHub Secrets)
- ✅ Can be customized with your own message & time

---

## 🧰 Tech Stack

- Python
- Twilio WhatsApp API
- GitHub Actions (Cron Scheduler)

---

## 📋 Prerequisites

Before starting, you must have:

- A **GitHub account**
- A **Twilio account**
- A verified **WhatsApp number**

---

## 🛠️ Setup Guide

### Step 1: Create Twilio WhatsApp Sandbox

1. Login to **Twilio**
2. Go to: Messaging → Try it out → WhatsApp Sandbox
3. Copy the sandbox number and join code
4. Send the join code to that number from your WhatsApp

---

### Step 2: Create GitHub Repository

1. Login to GitHub
2. Click **New repository**
3. Name it anything (example: `whatsapp-reminder-bot`)
4. Select:
- Public
- Add README
5. Create repository

---

### Step 3: Add Python Script

Create a file in repo named:


Paste this code:

```python
from twilio.rest import Client
import os
import datetime

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM")
TO_NUMBER = os.getenv("TWILIO_TO")

.
.
.for this check the repo and dont forget to star this repo if it helps
.
.
.
.

print("Message sent successfully!")
```

Repository → Settings → Secrets and variables → Actions


Add these secrets:

Name	|  Value
TWILIO_SID  |	Your Twilio Account SID
TWILIO_TOKEN    |	Your Twilio Auth Token
TWILIO_FROM |	whatsapp:+1xxxxxxxxxx
TWILIO_TO   |	whatsapp:+91XXXXXXXXXX

## Via docker Test Your Image from Anywhere

On any machine:
```
docker pull your_dockerhub_username/whatsapp-remainder
```

Then Run:
```
docker run \
-e TWILIO_SID=ACxxxxx \
-e TWILIO_TOKEN=xxxxx \
-e TWILIO_FROM=whatsapp:+1xxxxxxxxxx \
-e TWILIO_TO=whatsapp:+91xxxxxxxxxx \
your_dockerhub_username/whatsapp-remainder
```

## we are DevOps Ready🧠

You now have:

- ✅ Cloud-ready container
- ✅ Secure secrets handling
- ✅ Reusable deployment
- ✅ Docker Hub public image

## ⚠️ Important Notes


- Twilio free sandbox requires the receiver to join sandbox
- GitHub scheduled jobs may be delayed by a few minutes.

## 📌 Customization

- Change message in whatsapp_reminder.py
- Change time using cron in .yml
- Add multiple reminders.


## 🤝 Contributing

- Feel free to fork and modify this project.