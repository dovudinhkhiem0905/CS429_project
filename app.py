from flask import Flask, request, jsonify
import pickle
import os
import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Load TF-IDF Vectorizer and Matrix
if not os.path.exists('tfidf_vectorizer.pkl') or not os.path.exists('tfidf_matrix.pkl'):
    raise FileNotFoundError("TF-IDF model files not found.")
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

# Load Word2Vec Model and FAISS Index
if not os.path.exists('word2vec.model') or not os.path.exists('faiss_index.idx'):
    raise FileNotFoundError("Word2Vec model or FAISS index files not found.")
word2vec_model = Word2Vec.load("word2vec.model")
faiss_index = faiss.read_index("faiss_index.idx")

@app.route('/search', methods=['POST'])
def search():
    try:
        # Get JSON data with optional 'top_k' and mode
        json_input = request.get_json(force=True)
        query = json_input.get('query')
        top_k = json_input.get('top_k', 5)  # Default to top 5 results
        mode = json_input.get('mode', 'tfidf')  # Default to 'tfidf', alternative is 'word2vec'

        if not query:
            return jsonify({'error': 'No query provided'}), 400

        if mode == 'tfidf':
            # Process using TF-IDF
            query_vec = vectorizer.transform([query])
            cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
            doc_indices = cosine_similarities.argsort()[-top_k:][::-1]
        elif mode == 'word2vec':
            # Process using Word2Vec and FAISS
            query_tokens = word_tokenize(query.lower())
            query_vector = np.mean([word2vec_model.wv[word] for word in query_tokens if word in word2vec_model.wv], axis=0)
            _, doc_indices = faiss_index.search(np.array([query_vector]), top_k)
        else:
            return jsonify({'error': 'Invalid search mode specified'}), 400

        return jsonify({'results': doc_indices.tolist()}), 200

    except KeyError as e:
        return jsonify({'error': 'Missing data in request: ' + str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error processing the request: ' + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
