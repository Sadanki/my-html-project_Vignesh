Here's a **complete and clear step-by-step guide** for  CI/CD pipeline using **Bash**, **Python**, **crontab**, and **AWS EC2** to deploy a static HTML site with **Nginx**:

---

## ✅ Project: CI/CD Pipeline for Static HTML with Bash, Python, Crontab, and Nginx

GitHub Repo: [Sadanki/my-html-project\_Vignesh](https://github.com/Sadanki/my-html-project_Vignesh)

---

### 🔧 **Task 1: Set Up a Simple HTML Project**

1. Create a simple `index.html` file:

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head><title>My Portfolio</title></head>
<body>
  <h1>Hello from my CI/CD Pipeline!</h1>
</body>
</html>
```

2. Initialize Git and push to GitHub:

```bash
git init
git add index.html
git commit -m "Initial commit"
git remote add origin https://github.com/Sadanki/my-html-project_Vignesh.git
git push -u origin main
```

---

### ☁️ **Task 2: Set Up AWS EC2 (Ubuntu/Linux) with Nginx**

1. Launch an EC2 instance (Ubuntu).
2. SSH into the instance:

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

3. Update and install Nginx:

```bash
sudo apt update
sudo apt install nginx -y
```

4. Start Nginx and verify:

```bash
sudo systemctl start nginx
```

Browse to `http://<your-ec2-public-ip>` to see the default Nginx page.

---

### 🐍 **Task 3: Python Script to Check for New Commits**

1. Create a Python script: `check_commits.py`

```python
import requests
import os

REPO = "Sadanki/my-html-project_Vignesh"
API_URL = f"https://api.github.com/repos/{REPO}/commits"
BRANCH = "main"
LAST_COMMIT_FILE = "/home/ubuntu/last_commit.txt"

def get_latest_commit():
    response = requests.get(f"{API_URL}?sha={BRANCH}")
    response.raise_for_status()
    return response.json()[0]['sha']

def read_last_commit():
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, 'r') as f:
            return f.read().strip()
    return None

def write_last_commit(commit_sha):
    with open(LAST_COMMIT_FILE, 'w') as f:
        f.write(commit_sha)

def main():
    latest_commit = get_latest_commit()
    last_commit = read_last_commit()
    if latest_commit != last_commit:
        os.system("/home/ubuntu/deploy.sh")
        write_last_commit(latest_commit)

if __name__ == "__main__":
    main()
```

> 🔁 This checks for new commits and triggers deployment.

---

### 💻 **Task 4: Bash Script to Deploy the Code**

1. Create a file `deploy.sh` in `/home/ubuntu/`:

```bash
#!/bin/bash

cd /var/www/html
sudo rm -rf my-html-project_Vignesh
git clone https://github.com/Sadanki/my-html-project_Vignesh.git
sudo cp my-html-project_Vignesh/index.html /var/www/html/index.html
sudo systemctl restart nginx
```

2. Make it executable:

```bash
chmod +x /home/ubuntu/deploy.sh
```

---

### ⏱️ **Task 5: Set Up a Cron Job**

1. Edit crontab:

```bash
crontab -e
```

2. Add this line to run the Python script every 5 minutes:

```bash
*/5 * * * * /usr/bin/python3 /home/ubuntu/check_commits.py
```

> 📝 Make sure Python is installed: `sudo apt install python3-pip -y`

> 📝 You may need to install `requests`:

```bash
pip3 install requests
```

---

### ✅ **Task 6: Test the Setup**

1. Make a new commit to your GitHub repo:

```bash
echo "<p>New update at $(date)</p>" >> index.html
git add index.html
git commit -m "New update"
git push
```

2. Wait 5 minutes (or run `check_commits.py` manually) and refresh your EC2 IP in the browser. You should see the update.

---

## 📁 Recommended Folder Structure on EC2

```plaintext
/home/ubuntu/
├── check_commits.py
├── deploy.sh
├── last_commit.txt
```

---
