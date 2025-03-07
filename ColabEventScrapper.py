import os
import subprocess

# Function to clone the repo and install dependencies
def setup_repo():
    subprocess.run(["git", "clone", "https://github.com/alfakat/ColabEventScrapper.git"])
    os.chdir("ColabEventScrapper")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Function to create the email_settings.py file
def create_email_settings():
    secrets_content = f"""
SENDER_EMAIL = "{os.getenv('SENDER_EMAIL')}"
SENDER_PASSWORD = "{os.getenv('SENDER_PASSWORD')}"
RECIPIENT_EMAIL = "{os.getenv('RECIPIENT_EMAIL')}"
"""
    with open("email_settings.py", "w") as f:
        f.write(secrets_content)

# Function to run the main script
def run_main_script():
    subprocess.run(["python", "runer.py"])

def main():
    setup_repo()
    create_email_settings()
    run_main_script()

if __name__ == "__main__":
    main()
