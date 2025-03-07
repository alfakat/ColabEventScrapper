import json
import requests
from bs4 import BeautifulSoup


def scrape_events(sources: str):
    events = []

    with open(sources, 'r', encoding='utf-8') as f:
        sources = json.load(f)

    for source in sources:
        url = source['url']
        tag = source['tag']
        class_name = source['class_name']

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            events_list = soup.find_all(tag, class_=class_name)

            for event in events_list:
                parse_event(event, events)

        except Exception as e:
            print(f"Error fetching events from {url} {e}")

    return events


def parse_event(event, events):
    try:
        text = event.text.strip()
        link = event.contents[1].attrs['href']
        events.append({'text': text, 'link': link})
    except (IndexError, AttributeError):
        try:
            text = event.contents[0].text.strip()
            link = event.contents[0].contents[1]['href']
            events.append({'text': text, 'link': link})
        except (IndexError, AttributeError):
            print("Failed to extract text and link from event.")
