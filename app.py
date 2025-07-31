from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import schedule
import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from twilio.rest import Client  # Uncomment if using Twilio
import config
import sys
import requests

def log(msg):
    if getattr(config, 'ENABLE_LOGGING', False):
        print(f"[LOG] {msg}")

def click_next(wait):
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @name='Command' and @value='Next']")))
    next_button.click()
    time.sleep(getattr(config, 'PAGE_LOAD_DELAY', 3))  # Wait after navigation

def check_appointments():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = None
    try:
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            log('Could not start ChromeDriver. Make sure Chrome and ChromeDriver are installed and on your PATH.')
            log(str(e))
            return
        driver.get(config.TARGET_URL)
        time.sleep(getattr(config, 'PAGE_LOAD_DELAY', 3))  # Wait after initial navigation
        wait = WebDriverWait(driver, 10)
        try:
            # Step 1: Set language to English if not already
            log('Step 1: Checking/setting language to English')
            lang_select = wait.until(EC.presence_of_element_located((By.NAME, 'Language')))
            select = Select(lang_select)
            if select.first_selected_option.get_attribute('value') != 'en':
                select.select_by_value('en')
                change_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @name='Command' and @value='Change']")))
                change_btn.click()
                time.sleep(getattr(config, 'PAGE_LOAD_DELAY', 3))
                log('Language changed to English')
            else:
                log('Language already set to English')
            # Step 2: Select embassy office
            log(f"Step 2: Selecting embassy office '{config.EMBASSY_OFFICE}'")
            office_select = wait.until(EC.presence_of_element_located((By.NAME, 'Office')))
            select = Select(office_select)
            select.select_by_visible_text(config.EMBASSY_OFFICE)
            click_next(wait)
            # Step 3: Select visa type
            log(f"Step 3: Selecting visa type '{config.VISA_TYPE}'")
            visa_select = wait.until(EC.presence_of_element_located((By.NAME, 'CalendarId')))
            select = Select(visa_select)
            found = False
            for option in select.options:
                if config.VISA_TYPE in option.text:
                    select.select_by_visible_text(option.text)
                    found = True
                    break
            if not found:
                log('Visa type not found!')
                return
            click_next(wait)
            # Step 4: Next (third page)
            log('Step 4: Proceeding to next (third page)')
            click_next(wait)
            # Step 5: Next (fourth page)
            log('Step 5: Proceeding to next (fourth page)')
            click_next(wait)
            # Step 6: Check for appointment availability
            log('Step 6: Checking for appointment availability on the fifth page')
            try:
                # Look for the specific error message element
                no_appt_elem = driver.find_element(By.XPATH, f"//p[@class='message-error' and contains(text(), '{config.KEYWORD_TO_SEARCH}')]")
                log('No appointments available.')
                if getattr(config, 'SEND_EMAIL_IF_NONE', False):
                    log('Sending notification: No appointments available.')
                    send_email_notification(available=False)
            except NoSuchElementException:
                log('Appointment found! Sending notification.')
                send_email_notification(available=True)
                # send_sms_notification()  # Uncomment if using SMS
        except Exception as e:
            log(f'Error during workflow: {e}')
    except Exception as e:
        log(f'Critical error in check_appointments: {e}')
    finally:
        if driver is not None:
            try:
                driver.quit()
            except Exception as e:
                log(f'Error closing browser: {e}')

def send_telegram_notification(message):
    if not getattr(config, 'ENABLE_TELEGRAM', False):
        return
    try:
        url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": message
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            log('Telegram notification sent!')
        else:
            log(f'Failed to send Telegram notification: {response.text}')
    except Exception as e:
        log(f'Error sending Telegram notification: {e}')

def send_email_notification(available=True):
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_SENDER
    msg['To'] = config.EMAIL_RECEIVER
    if available:
        msg['Subject'] = 'Embassy Appointment Available!'
        body = f"An appointment slot may be available at {config.TARGET_URL}"
    else:
        msg['Subject'] = 'No Embassy Appointments Available'
        body = f"There are currently no appointments available at {config.TARGET_URL}"
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        server.sendmail(config.EMAIL_SENDER, config.EMAIL_RECEIVER, msg.as_string())
        server.quit()
        log('Email notification sent!')
    except Exception as e:
        log(f'Failed to send email: {e}')
    # Send Telegram notification if enabled
    send_telegram_notification(body)

# def send_sms_notification():
#     client = Client(config.TWILIO_SID, config.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         body=f"Embassy appointment may be available! {config.TARGET_URL}",
#         from_=config.TWILIO_PHONE,
#         to=config.YOUR_PHONE
#     )
#     log('SMS notification sent!')

# def main():
#     schedule.every(config.REFRESH_INTERVAL_MINUTES).minutes.do(check_appointments)
#     print(f'Bot started. Monitoring for appointments every {config.REFRESH_INTERVAL_MINUTES} minutes...')
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == '__main__':
#     main() 


def main():
    print('Bot started.')
    while True:
        check_appointments()

        if getattr(config, 'USE_RANDOM_INTERVAL', False):
            interval = random.uniform(
                getattr(config, 'RANDOM_INTERVAL_MIN', 1),
                getattr(config, 'RANDOM_INTERVAL_MAX', 3)
            )
            seconds = int(interval * 60)
            log(f"Waiting {seconds} seconds before next check (randomized)...")
            time.sleep(seconds)
        else:
            interval = getattr(config, 'REFRESH_INTERVAL_MINUTES', 1)
            seconds = int(interval * 60)
            log(f"Waiting {seconds} seconds before next check (fixed interval)...")
            time.sleep(seconds)

if __name__ == '__main__':
    main()