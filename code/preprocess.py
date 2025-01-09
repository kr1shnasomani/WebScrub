import json
import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Dict, List, Set, Union
from pathlib import Path
import logging
from collections import defaultdict

class ContentPreprocessor:
    def __init__(self, model_name: str = "en_core_web_sm"):
        self.nlp = spacy.load(model_name)
        self.setup_filters()
    
    def setup_filters(self):
        self.boilerplate_terms: Set[str] = {
            "menu", "sidebar", "navigate", "footer", "header", "main",
            "click", "link", "button", "scroll", "navigation",
            "cookie", "privacy", "terms", "copyright", "rights", "reserved",
            "login", "signup", "sign", "register",
            "upload", "download", "file", "image", "png", "jpg", "svg",
            "portal", "special", "help", "contact", "about", "search",
            "community", "donate", "contribution",
            "window", "browser", "page", "site", "website", "content",
            "mobile", "desktop", "view", "display", "screen",
            "visit", "browse", "edit", "share", "save", "delete",
            "submit", "cancel", "accept", "reject"
        }
        
        self.patterns = {
            'url': re.compile(r'https?://\S+|www\.\S+'),
            'file': re.compile(r'\.[a-zA-Z]{2,4}$'),
            'html': re.compile(r'<[^>]+>'),
            'special_chars': re.compile(r'[^\w\s-]'),
            'multiple_spaces': re.compile(r'\s+')
        }

    def is_meaningful_sentence(self, sentence: str) -> bool:
        min_words = 5
        min_chars = 20
        words = sentence.split()
        
        if len(words) < min_words or len(sentence) < min_chars:
            return False
            
        meaningful_words = [w for w in words if w.lower() not in self.boilerplate_terms]
        if len(meaningful_words) < len(words) * 0.5:
            return False
            
        return True
    
    def extract_meaningful_content(self, text: str) -> List[Dict[str, Union[str, List[str]]]]:
        doc = self.nlp(text)
        meaningful_sections = []
        
        for sent in doc.sents:
            clean_sent = self.clean_text(sent.text)
            if self.is_meaningful_sentence(clean_sent):
                terms = [token.lemma_ for token in sent 
                        if not token.is_stop 
                        and token.is_alpha 
                        and len(token.text) > 2
                        and token.lemma_.lower() not in self.boilerplate_terms]
                
                if terms:
                    meaningful_sections.append({
                        "text": clean_sent,
                        "key_terms": terms,
                        "entities": [(ent.text, ent.label_) for ent in sent.ents]
                    })
        
        return meaningful_sections

    def clean_text(self, text: str) -> str:
        text = self.patterns['html'].sub(' ', text)
        text = self.patterns['url'].sub(' ', text)
        text = self.patterns['special_chars'].sub(' ', text)
        text = self.patterns['multiple_spaces'].sub(' ', text)
        return text.strip()

    def process_content(self, content: Dict[str, str]) -> Dict[str, Dict]:
        processed_data = {}
        
        for key, text in content.items():
            if not isinstance(text, str) or not text.strip():
                continue
                
            meaningful_sections = self.extract_meaningful_content(text)
            
            if meaningful_sections:
                all_terms = " ".join([
                    " ".join(section["key_terms"]) 
                    for section in meaningful_sections
                ])
                
                vectorizer = TfidfVectorizer(max_features=10)
                tfidf_matrix = vectorizer.fit_transform([all_terms])
                keywords = list(vectorizer.get_feature_names_out())
                
                entities = defaultdict(set)
                for section in meaningful_sections:
                    for ent_text, ent_label in section["entities"]:
                        entities[ent_label].add(ent_text)
                
                processed_data[key] = {
                    "sections": meaningful_sections,
                    "keywords": keywords,
                    "entities": {k: list(v) for k, v in entities.items()},
                    "statistics": {
                        "section_count": len(meaningful_sections),
                        "unique_terms": len(set(term for section in meaningful_sections 
                                              for term in section["key_terms"]))
                    }
                }
        
        return processed_data

def process_file(input_path: str, output_path: str):
    processor = ContentPreprocessor()
    
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        processed_data = processor.process_content(
            data if isinstance(data, dict) else {"content": str(data)}
        )
        
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(processed_data, file, indent=4, ensure_ascii=False)
            
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        raise

if __name__ == "__main__":
    input_path = r"C:\Users\krish\OneDrive\Desktop\Projects\WebScrub - Web Scraper\output\text.json"
    output_path = r"C:\Users\krish\OneDrive\Desktop\Projects\WebScrub - Web Scraper\output\preprocessed.json"
    process_file(input_path, output_path)