#!/bin/bash
# Go to working directory
cd ~/ci-cd-html

# Remove old site
rm -rf site
mkdir site

# Clone latest code
git clone https://github.com/Sadanki/my-html-project_Vignesh.git site

# Copy HTML files to Nginx directory
sudo cp -r site/* /var/www/html/

# Restart Nginx
sudo systemctl restart nginx
