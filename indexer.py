from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

# Function to extract text from HTML content
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

# Function to create a TF-IDF index from a list of documents
def create_tfidf_index(docs):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    return vectorizer, tfidf_matrix

# Function to save the TF-IDF vectorizer and matrix to disk
def save_index(vectorizer, tfidf_matrix):
    with open('tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)

# Example usage: Load documents, extract text, and create an index
if __name__ == "__main__":
    # Directory containing HTML documents
    html_directory = 'path/to/html/files'

    # Read HTML documents from the directory
    documents = []
    for filename in os.listdir(html_directory):
        if filename.endswith('.html'):
            filepath = os.path.join(html_directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                html_content = file.read()
                text = extract_text_from_html(html_content)
                documents.append(text)

    # Create a TF-IDF index from the extracted text
    if documents:
        vectorizer, tfidf_matrix = create_tfidf_index(documents)
        save_index(vectorizer, tfidf_matrix)
        print("TF-IDF vectorizer and matrix have been saved.")
    else:
        print("No documents found or all documents are empty.")
