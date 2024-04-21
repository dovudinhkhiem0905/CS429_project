import os
import logging
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to extract text from HTML content
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def create_tfidf_index(docs):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    feature_names = vectorizer.get_feature_names_out()
    
    # Log each term with its corresponding TF-IDF score for the first document as an example
    for doc_idx in range(tfidf_matrix.shape[0]):
        logging.info(f"Document {doc_idx + 1} TF-IDF Scores:")
        doc_vector = tfidf_matrix[doc_idx]
        terms = feature_names[doc_vector.indices]
        scores = doc_vector.data
        for term, score in zip(terms, scores):
            logging.info(f"{term}: {score}")

    return vectorizer, tfidf_matrix


# Function to save the TF-IDF vectorizer and matrix to disk
def save_index(vectorizer, tfidf_matrix):
    with open('tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)

if __name__ == "__main__":
    html_directory = 'web_crawler/output'
    documents = []
    
    # Read HTML documents from the directory
    for filename in os.listdir(html_directory):
        if filename.endswith('.html'):
            filepath = os.path.join(html_directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                html_content = file.read()
                text = BeautifulSoup(html_content, 'html.parser').get_text()
                documents.append(text)
    
    if documents:
        vectorizer, tfidf_matrix = create_tfidf_index(documents)
        with open('tfidf_vectorizer.pkl', 'wb') as f:
            pickle.dump(vectorizer, f)
        with open('tfidf_matrix.pkl', 'wb') as f:
            pickle.dump(tfidf_matrix, f)
        logging.info("TF-IDF vectorizer and matrix have been saved.")
    else:
        logging.info("No documents found or all documents are empty.")

