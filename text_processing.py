import faiss
import numpy as np
from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess_documents(docs):
    return [word_tokenize(doc.lower()) for doc in docs]

def train_word2vec(processed_docs, vector_size=100, window=5, min_count=1, workers=4):
    model = Word2Vec(sentences=processed_docs, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    model.save("word2vec.model")
    return model

def create_faiss_index(word2vec_model, processed_docs):
    dimension = word2vec_model.vector_size
    faiss_index = faiss.IndexFlatL2(dimension)
    doc_vectors = []

    for doc in processed_docs:
        if doc:  # Ensure the document is not empty
            doc_vector = np.mean([word2vec_model.wv[word] for word in doc if word in word2vec_model.wv], axis=0, keepdims=True)
            if doc_vector.size > 0:
                doc_vectors.append(doc_vector)

    if doc_vectors:  # Check if there are any vectors to add
        faiss_index.add(np.concatenate(doc_vectors, axis=0))
        faiss.write_index(faiss_index, "faiss_index.idx")

    return faiss_index

if __name__ == "__main__":
    docs = ["Hello world", "Hello from the other side", "Another example document"]
    processed_docs = preprocess_documents(docs)
    word2vec_model = train_word2vec(processed_docs)
    faiss_index = create_faiss_index(word2vec_model, processed_docs)
    print("Index created and saved successfully.")
