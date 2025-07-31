import os
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# URL of the embassy appointment page
TARGET_URL = os.getenv("TARGET_URL", "https://appointment.bmeia.gv.at/")

# Text that means 'no appointment available'
KEYWORD_TO_SEARCH = os.getenv("KEYWORD_TO_SEARCH", "For your selection there are unfortunately no appointments available")

# Gmail credentials for sending email alerts
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# (Optional) Twilio SMS configuration
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
YOUR_PHONE = os.getenv("YOUR_PHONE")

# Embassy office to select (e.g., 'KAIRO')
EMBASSY_OFFICE = os.getenv("EMBASSY_OFFICE", "KAIRO")

# Visa type to select (e.g., 'Aufenthaltsbewilligung Student (nur Bachelor)')
VISA_TYPE = os.getenv("VISA_TYPE", "Aufenthaltsbewilligung Student (nur Bachelor)")

# Refresh interval in minutes
REFRESH_INTERVAL_MINUTES = float(os.getenv("REFRESH_INTERVAL_MINUTES", "0.5"))

# Use random refresh intervals instead of fixed?
USE_RANDOM_INTERVAL = os.getenv("USE_RANDOM_INTERVAL", "True").lower() in ('true', '1', 't')

# Random interval range (in minutes)
RANDOM_INTERVAL_MIN = int(os.getenv("RANDOM_INTERVAL_MIN", "1"))
RANDOM_INTERVAL_MAX = int(os.getenv("RANDOM_INTERVAL_MAX", "3"))

# Enable detailed logging of workflow steps
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() in ('true', '1', 't')

# Send email notification even if there are no appointments
SEND_EMAIL_IF_NONE = os.getenv("SEND_EMAIL_IF_NONE", "True").lower() in ('true', '1', 't')

# Delay (in seconds) after each page navigation
PAGE_LOAD_DELAY = int(os.getenv("PAGE_LOAD_DELAY", "3"))

# Telegram notification configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ENABLE_TELEGRAM = os.getenv("ENABLE_TELEGRAM", "True").lower() in ('true', '1', 't')

# Add python-dotenv to requirements.txt for local development
# so the user can create a .env file.
# I'll also need to add it to requirements.txt
# For Render, the user will set env vars in the dashboard.
# I will handle requirements.txt later.
