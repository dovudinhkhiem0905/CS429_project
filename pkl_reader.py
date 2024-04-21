import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Load the TF-IDF matrix
with open('tfidf_matrix.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

# Get feature names to use as DataFrame column headers
feature_names = vectorizer.get_feature_names_out()

# Convert sparse matrix to dense matrix
dense_tfidf_matrix = tfidf_matrix.todense()

# Create a DataFrame
df = pd.DataFrame(dense_tfidf_matrix, columns=feature_names)

# Calculate the average TF-IDF score for each term
term_avg_scores = df.mean().sort_values(ascending=False)

# Display the top 20 terms with the highest average TF-IDF scores
print(term_avg_scores.head(20))

# Plot the top 20 terms
plt.figure(figsize=(12, 8))
term_avg_scores.head(20).plot(kind='bar')
plt.title('Top 20 Terms by Average TF-IDF Score')
plt.xlabel('Terms')
plt.ylabel('Average TF-IDF Score')
plt.show()

