<h1 align="center">WebScrub</h1>
This project is a modular pipeline for web scraping, text cleaning, and NLP-based analysis. It extracts meaningful content, keywords, entities, and statistics from websites using Selenium, spaCy and TF-IDF. Outputs include structured JSON files for insights, suitable for content analysis, research and NLP-driven applications.

## Execution Guide:
1. Run the following command in the terminal:
   ```
   pip install requests selenium html2text spacy scikit-learn
   ```

2. Go to the site **https://googlechromelabs.github.io/chrome-for-testing/** and install ChromeDriver
   Note: Make sure the ChromeDriver you are using is the same version as the Google Chrome. If not your code will output an error.

3. Copy and paste the path of the ChromeDrive in the code in `scraper.py`

4. Enter the link of the page whose data you want to get scrapped in `scraper.py`

5. Run `scraper.py` and it will give `html.json` file as an output with the HTML content of the page

6. Copy the path of `html.json` file and the place you want to store the resultant file (clean text file) and paste it in the `htmltotext.py` code

7. Upon running this script it will output a file named `text.json` (this file contains the clean text)

8. Now if the path of this `text.json` is entered into the code `preprocess.py` code then it outputs a pre-processed file named `preprocessed.json`

## Overview:
The project implements a modular system to scrape web content, process it into clean, readable formats, and extract meaningful information using Natural Language Processing (NLP) techniques. The pipeline is structured into three distinct components, each addressing a specific stage in the content lifecycle.

### **1. Scraper Component (scraper.py)**

**Purpose**: To scrape web content from dynamic or static websites.

- **Key Features**:
  - **Dynamic Content Handling**: Uses Selenium WebDriver for rendering JavaScript-based dynamic web pages.
  - **Static Content Handling**: Uses `requests` for straightforward HTTP requests to fetch HTML content.
  - **Output**: Saves the raw HTML content as a JSON file for further processing.

- **Workflow**:
  1. Determines the type of web page (dynamic/static).
  2. Fetches the HTML content.
  3. Saves the content to a specified JSON file.

### **2. HTML-to-Text Conversion (htmltotext.py)**

**Purpose**: To clean and convert raw HTML content into plain text while preserving critical formatting and information.

- **Key Features**:
  - **Preservation**: Links, images, and emphasis are retained.
  - **Customization**: Optional ignoring of specific HTML elements like links and images.
  - **Output**: Saves cleaned text as JSON for downstream processing.

- **Workflow**:
  1. Reads raw HTML content from the scraper's output.
  2. Uses `html2text` to convert HTML into readable plain text.
  3. Saves the cleaned text as a JSON file.

### **3. Preprocessing and NLP Pipeline (preprocess.py)**

**Purpose**: To extract meaningful content, key terms, entities, and statistics from the cleaned text.

- **Key Features**:
  - **Text Cleaning**: Removes URLs, HTML tags, special characters, and boilerplate terms (e.g., "menu," "click").
  - **NLP-Based Processing**: Utilizes spaCy for tokenization, lemmatization, and Named Entity Recognition (NER).
  - **Meaningful Content Extraction**: Filters out uninformative sentences using criteria like word count, length, and relevance.
  - **TF-IDF Analysis**: Identifies top keywords using TF-IDF Vectorizer.
  - **Entity Categorization**: Groups named entities (e.g., "PERSON," "ORG") into categories.
  - **Statistics**: Computes statistics like the number of meaningful sections and unique terms.
  - **Output**: Saves processed data as JSON for easy integration into downstream tasks.

- **Workflow**:
  1. Reads the cleaned text from the HTML-to-text component's output.
  2. Processes content to extract:
     - Meaningful sentences.
     - Key terms (lemmas of informative words).
     - Named entities with categories.
  3. Generates keywords and statistics for summarization.
  4. Saves the processed data into a structured JSON file.

This project demonstrates a robust pipeline to transform raw web content into actionable insights, suitable for applications in content analytics, research, and NLP-driven solutions.
