import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import numpy as np

# Load the Word2Vec model
model = Word2Vec.load("word2vec.model")

# Extract words and corresponding vectors
words = list(model.wv.key_to_index.keys())
vectors = np.array([model.wv[word] for word in words])

# Apply PCA
pca = PCA(n_components=2)
vectors_pca = pca.fit_transform(vectors)

# Adjust perplexity dynamically based on the number of vectors
perplexity_value = min(30, len(vectors) - 1)  # Ensuring perplexity is less than the number of samples

# Apply t-SNE with adjusted perplexity
tsne = TSNE(n_components=2, init='pca', n_iter=2500, random_state=23, perplexity=perplexity_value)
vectors_tsne = tsne.fit_transform(vectors)

# Plotting function
def plot_embeddings(vectors, labels, title):
    plt.figure(figsize=(12, 12))
    plt.scatter(vectors[:, 0], vectors[:, 1], c='green', edgecolors='k')
    for i, word in enumerate(labels):
        plt.annotate(word, xy=(vectors[i, 0], vectors[i, 1]))
    plt.title(title)
    plt.grid(True)
    plt.show()

# Plot PCA
plot_embeddings(vectors_pca, words, "Word2Vec Embeddings Visualization with PCA")

# Plot t-SNE
plot_embeddings(vectors_tsne, words, "Word2Vec Embeddings Visualization with t-SNE")


import faiss
import numpy as np

# Load the FAISS index
index = faiss.read_index("faiss_index.idx")

# Choose a query vector from the Word2Vec model
query_word = 'example'

if query_word in model.wv.key_to_index:
    query_vector = model.wv[query_word].reshape(1, -1)
    # Continue with querying FAISS index or other operations
else:
    print(f"The word '{query_word}' is not in the vocabulary.")

query_vector = model.wv[query_word].reshape(1, -1)

# Query the FAISS index for the top 10 nearest neighbors
D, I = index.search(query_vector, 10)

# Print the query results
print("Query Results for word:", query_word)
for i in range(len(I[0])):
    similar_word = words[I[0][i]]
    distance = D[0][i]
    print(f"{i+1}: {similar_word} (Distance: {distance})")

