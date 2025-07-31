# Embassy Appointment Monitor Bot (MVP)

## 🎯 Project Goal

Create a Python bot that automatically monitors a specific embassy appointment booking webpage. The bot checks if appointments become available and sends a notification (via email or optional SMS) when they do. It runs every few minutes using a scheduler and can be deployed for continuous operation on a free service like Heroku.

---

## ✅ MVP Features

- 🕸 Scrapes a target embassy website page.
- 🔎 Detects when appointments become available (by checking for absence of a specific keyword).
- 📬 Sends notifications via **Gmail email**.
- 📲 (Optional) Sends SMS notifications via **Twilio**.
- 🔁 Automatically runs every 10–15 minutes.
- ☁️ Can be deployed on **Heroku** with a scheduler.

---

## ⚙️ Project Structure

appointment-bot/
│
├── app.py # Main logic: scraping, checking, notifying
├── config.py # Stores credentials and URLs
├── requirements.txt # Python packages needed
├── Procfile # Heroku process definition
└── runtime.txt # (Optional) Python version for Heroku


---

## 🔁 How the Bot Works

1. Every 10 minutes, the bot fetches the embassy appointment page (URL provided by user).
2. It scans the page for a specific **"no appointment" keyword** (e.g., “No appointments available”).
3. If that keyword **is not found**, the bot assumes appointments are available.
4. It sends a **notification email** (or optional SMS).
5. This repeats automatically using a scheduler like `schedule` or Heroku Scheduler.

---

## 🧩 Configuration (`config.py`)

To make the bot reusable and customizable, all important values should be added by the user in `config.py`:

| Variable             | Description                                        |
|----------------------|----------------------------------------------------|
| `TARGET_URL`         | URL of the embassy appointment page                |
| `KEYWORD_TO_SEARCH`  | Text to search for that means "no appointment"     |
| `EMAIL_SENDER`       | Gmail address used to send alerts                  |
| `EMAIL_PASSWORD`     | Gmail **App Password** (not your regular password) |
| `EMAIL_RECEIVER`     | The target email to receive notifications          |
| `TWILIO_SID`         | *(Optional)* Twilio Account SID for SMS            |
| `TWILIO_AUTH_TOKEN`  | *(Optional)* Twilio Auth Token                     |
| `TWILIO_PHONE`       | *(Optional)* Twilio phone number                   |
| `YOUR_PHONE`         | *(Optional)* Your personal phone number            |

---

## 🛠 Deployment (Optional: Heroku)

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login via terminal: `heroku login`
3. Create and deploy the app:
   ```bash
   git init
   heroku create appointment-checker
   git add .
   git commit -m "Initial commit"
   git push heroku master
4. Add Heroku Scheduler:

Go to Heroku Dashboard → Resources → Add-ons → Search “Heroku Scheduler” → Add.
Create a job: python app.py every 10 minutes.

📬 Notification Methods
Email (via Gmail SMTP)
Must enable App Passwords in Gmail settings.

Bot logs in via smtplib and sends a simple email when a slot is found.

SMS (Optional, via Twilio)
Uses Twilio Python SDK.

Twilio account and credits required.