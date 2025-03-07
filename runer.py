from email_notification import  send_email
from scrape_events import scrape_events

"""
Runer of ColabEventScraper
"""

if __name__ == "__main__":
    events = scrape_events(sources = 'sources.json')
    if events:
        send_email(events)
    else:
        print("No events found.")