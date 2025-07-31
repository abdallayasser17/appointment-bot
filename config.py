# Configuration for Embassy Appointment Monitor Bot

# URL of the embassy appointment page
TARGET_URL = "https://appointment.bmeia.gv.at/"

# Text that means 'no appointment available' (e.g., 'No appointments available')
KEYWORD_TO_SEARCH = "For your selection there are unfortunately no appointments available"

# Gmail credentials for sending email alerts
EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.environ.get('EMAIL_RECEIVER')

# (Optional) Twilio SMS configuration
TWILIO_SID = "your_twilio_sid"  # Twilio Account SID
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"  # Twilio Auth Token
TWILIO_PHONE = "+1234567890"  # Twilio phone number
YOUR_PHONE = "+0987654321"    # Your personal phone number 

# Embassy office to select (e.g., 'KAIRO')
EMBASSY_OFFICE = os.environ.get('EMBASSY_OFFICE')

# Visa type to select (e.g., 'Aufenthaltsbewilligung Student (nur Bachelor)')
VISA_TYPE = os.environ.get('VISA_TYPE')

# Refresh interval in minutes (how often to check for appointments)
REFRESH_INTERVAL_MINUTES = int(os.environ.get('REFRESH_INTERVAL_MINUTES', 1))

# 🔁 Use random refresh intervals instead of fixed?
USE_RANDOM_INTERVAL = os.environ.get('USE_RANDOM_INTERVAL', 'False') == 'True'

# ⏱️ Random interval range (in minutes)
RANDOM_INTERVAL_MIN = float(os.environ.get('RANDOM_INTERVAL_MIN', 1))
RANDOM_INTERVAL_MAX = float(os.environ.get('RANDOM_INTERVAL_MAX', 3))

# Enable detailed logging of workflow steps
ENABLE_LOGGING = os.environ.get('ENABLE_LOGGING', 'False') == 'True'

# Send email notification even if there are no appointments (set to True to always notify, False to only notify if available)
SEND_EMAIL_IF_NONE = os.environ.get('SEND_EMAIL_IF_NONE', 'False') == 'True'

# Delay (in seconds) after each page navigation to allow for slow internet or page loads
PAGE_LOAD_DELAY = int(os.environ.get('PAGE_LOAD_DELAY', 3)) 

# Telegram notification configuration
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
ENABLE_TELEGRAM = os.environ.get('ENABLE_TELEGRAM', 'False') == 'True'