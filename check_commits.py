import requests
import json
import os

REPO = "Sadanki/my-html-project_Vignesh"
BRANCH = "main"
STATE_FILE = "/home/ubuntu/ci-cd-html/last_commit.txt"

def get_latest_commit():
    url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['sha']
    return None

def read_last_commit():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as file:
            return file.read().strip()
    return None

def write_last_commit(sha):
    with open(STATE_FILE, 'w') as file:
        file.write(sha)

def main():
    latest_sha = get_latest_commit()
    last_sha = read_last_commit()

    if latest_sha and latest_sha != last_sha:
        print("New commit found! Deploying...")
        os.system("bash deploy.sh")
        write_last_commit(latest_sha)
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()
