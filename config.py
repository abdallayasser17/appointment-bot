# Configuration for Embassy Appointment Monitor Bot

# URL of the embassy appointment page
TARGET_URL = "https://appointment.bmeia.gv.at/"

# Text that means 'no appointment available' (e.g., 'No appointments available')
KEYWORD_TO_SEARCH = "For your selection there are unfortunately no appointments available"

# Gmail credentials for sending email alerts
EMAIL_SENDER = "ibrahimabdo1120002@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "huzs oesk xuau ipdf"    # Gmail App Password (not your regular password)
EMAIL_RECEIVER = "youssefalaa1112003@gmail.com"  # Where to send notifications

# (Optional) Twilio SMS configuration
TWILIO_SID = "your_twilio_sid"  # Twilio Account SID
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"  # Twilio Auth Token
TWILIO_PHONE = "+1234567890"  # Twilio phone number
YOUR_PHONE = "+0987654321"    # Your personal phone number 

# Embassy office to select (e.g., 'KAIRO')
EMBASSY_OFFICE = "KAIRO"

# Visa type to select (e.g., 'Aufenthaltsbewilligung Student (nur Bachelor)')
VISA_TYPE = "Aufenthaltsbewilligung Student (nur Bachelor)" 

# Refresh interval in minutes (how often to check for appointments)
REFRESH_INTERVAL_MINUTES = 0.5  # Change to your preferred interval

# 🔁 Use random refresh intervals instead of fixed?
USE_RANDOM_INTERVAL = True

# ⏱️ Random interval range (in minutes)
RANDOM_INTERVAL_MIN = 1
RANDOM_INTERVAL_MAX = 3

# Enable detailed logging of workflow steps
ENABLE_LOGGING = True 

# Send email notification even if there are no appointments (set to True to always notify, False to only notify if available)
SEND_EMAIL_IF_NONE = True 

# Delay (in seconds) after each page navigation to allow for slow internet or page loads
PAGE_LOAD_DELAY = 3 

# Telegram notification configuration
TELEGRAM_BOT_TOKEN = "8418988090:AAFRnZEqew9EUl6IShZPJ_LTVTK-FRYJDUY"
TELEGRAM_CHAT_ID = "1488253654"
ENABLE_TELEGRAM = True 