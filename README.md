# ColabEventScrapper
Do not miss any of your favourite events without daily checking event site!

## About project

Project that scrapes events from your favorite sites and sent email notification about
upcoming events on email. Set how often you would like to get notified and 
Colad will send it to your email box.

## Presettings

- clone the repo, choose interpreter (created with 3.9) and create venv
- install requirements.txt
- edit the sources.json: fill 'url' and 'class_name' fields
- set email_settings.py. Note, that SENDER_PASSWORD is not password of your account, but generated App password
- run runer.py and check your inbox :)

## Colab autoranning
- create Jupyter file in your Colab workspace and copy it to GitHub. See ColabEventScrapper.ipynb for reference 
- alternatively you may create Python file as well. See ColabEventScrapper.py for reference 
- go to 'Actions' tab in GitHub and create new workflow to run the runer.py when you wish. See colab-scheduler.yml as reference

## Author’s info
Please PM/mail me if you have comments or suggestions.
