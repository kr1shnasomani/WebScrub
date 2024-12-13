import json
import html2text

file_path = r"C:\Users\krish\OneDrive\Desktop\Projects\Web Scraper\html.json"
output_path = r"C:\Users\krish\OneDrive\Desktop\Projects\Web Scraper\text.json"

def clean_html_to_text(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = False 
    h.ignore_images = False  
    h.ignore_emphasis = False  
    h.body_width = 0 
    text = h.handle(html_content)
    return text.strip()

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = json.load(file)  
        cleaned_text = clean_html_to_text(html_content)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(cleaned_text, output_file, ensure_ascii=False, indent=4)  

    print(f"Cleaned text saved to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")    