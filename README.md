<h1 align="center">WebScrub</h1>
This project scrapes website data (both dynamic and static), processes the HTML content to retain links, images, and emphasis, and then cleans it. The cleaned text is saved in a structured JSON format for easy access and further processing.

## Execution Guide:
1. Run the following command in the terminal:
   ```
   pip install requests selenium beautifulsoup4 json html2text
   ```

2. Go to the site **https://googlechromelabs.github.io/chrome-for-testing/** and install ChromeDriver
   Note: Make sure the ChromeDriver you are using is the same version as the Google Chrome. If not your code will output an error.

3. Copy and paste the path of the ChromeDrive in the code in `scraper.py`

4. Enter the link of the page whose data you want to get scrapped in `scraper.py`

5. Run `scraper.py` and it will give `html.json` file as an output with the HTML content of the page

6. Copy the path of `html.json` file and the place you want to store the resultant file (clean text file) and paste it in the `htmltotext.py` code

7. Upon running this script it will output a file named `text.json` (this file contains the clean text)

## Overview:
The two code snippets together outline a complete process for scraping and converting website content from HTML to plain text.

1. **Web Scraping (Code 1)**:  
   - The `scrape_website` function fetches the content of a website. If the website is **static**, it uses `requests` to retrieve the HTML content. For **dynamic websites** (where content is loaded via JavaScript), the function uses **Selenium** with a Chrome WebDriver to load the page and capture the rendered HTML after it has fully loaded.  
   - After scraping the website, the content is saved to a JSON file (`html.json`) using the `save_content_to_json` function, which ensures the content is stored in a structured JSON format.

2. **HTML to Plain Text Conversion (Code 2)**:  
   - The second script processes the HTML content saved in `html.json`. It uses **`html2text`** to convert the HTML into readable plain text. The `HTML2Text` object is configured to retain links, images, and emphasis (bold/italic) while ensuring no text wrapping occurs (i.e., it avoids truncating lines). This results in the entire raw content being converted to a readable text format.
   - The cleaned text is then saved into a new JSON file (`text.json`), maintaining the structure but with plain text instead of HTML.

**Combined Workflow**:
   - First, **Code 1** scrapes the HTML content from a dynamic or static website and stores it in `html.json`.
   - Then, **Code 2** loads the HTML from the JSON file, converts it into plain text while preserving key elements like links and emphasis, and saves the cleaned text into a new file, `text.json`.

This two-step process allows for the efficient scraping of static and dynamic websites and the extraction of human-readable content from raw HTML.
