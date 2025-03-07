import re
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_settings import *

def extract_date(text):

    date_pattern = r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})|([A-Za-z]+\s\d{1,2},\s\d{4})'
    match = re.search(date_pattern, text)
    if match:

        return datetime.strptime(match.group(), '%d/%m/%Y') if '/' in match.group() else datetime.strptime(
            match.group(), '%B %d, %Y')
    return None


def send_email(events):

    events_with_dates = []
    for event in events:
        event_date = extract_date(event['text'])
        if event_date:
            events_with_dates.append({'text': event['text'], 'link': event['link'], 'date': event_date})


    events_with_dates.sort(key=lambda x: x['date'])

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Upcoming Events Notification"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL


    html_content = """
    <html>
    <body>
        <h2 style="color: #4CAF50;">Upcoming Events:</h2>
        <ul style="list-style-type: none; padding: 0;">
    """

    for event in events_with_dates:
        html_content += f"""
            <li style="margin-bottom: 10px;">
                <strong>{event['date'].strftime('%B %d, %Y')}</strong>: 
                <a href='{event['link']}' style="text-decoration: none; color: #1E90FF;">
                    {event['text']}
                </a>
            </li>
        """

    html_content += """
        </ul>
        <p style="font-size: 12px; color: #888;">This is an automated message. Please do not reply.</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")