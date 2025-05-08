<h1 align="center">WebScrub</h1>
This project is a modular pipeline for web scraping, text cleaning, and NLP-based analysis. It extracts meaningful content, keywords, entities, and statistics from websites using Selenium, spaCy and TF-IDF. Outputs include structured JSON files for insights, suitable for content analysis, research and NLP-driven applications.

## Execution Guide:
1. Clone the repository:
   ```
   git clone https://github.com/kr1shnasomani/WebScrub.git
   cd WebScrub
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download ChromeDriver:
   
   Go to **https://googlechromelabs.github.io/chrome-for-testing/** and install ChromeDriver

   Note: Make sure the ChromeDriver you are using is the same version as the Google Chrome. If not your code will output an error.

4. Copy and paste the path of the ChromeDrive in the code in `scraper.py`

5. Enter the link of the page whose data you want to get scrapped in `scraper.py`

6. Run `scraper.py` and it will give `html.json` file as an output with the HTML content of the page

7. Copy the path of `html.json` file and the place you want to store the resultant file (clean text file) and paste it in the `htmltotext.py` code

8. Upon running this script it will output a file named `text.json` (this file contains the clean text)

9. Now if the path of this `text.json` is entered into the code `preprocess.py` code then it outputs a pre-processed file named `preprocessed.json`
