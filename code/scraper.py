import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import time

driver_path = r"C:\Users\krish\OneDrive\Desktop\Projects\chromedriver.exe"

def scrape_website(url, dynamic=False, driver_path=driver_path):
    if not dynamic:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
    else:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        time.sleep(3) 
        content = driver.page_source
        driver.quit()
    
    return content

def save_content_to_json(content, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False, indent=4))

url = "https://en.wikipedia.org/wiki/Chess"
content = scrape_website(url, dynamic=True, driver_path=driver_path)

# Specify the desired file path
output_path = r"C:\Users\krish\OneDrive\Desktop\Projects\WebScrub - Web Scraper\output\html.json"
save_content_to_json(content, output_path)

print(f"HTML text saved to {output_path}")