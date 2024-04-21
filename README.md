# Information Retrieval System with Neural Search Capabilities

### ***Note: Report is below description! Please refer to report.docx in the repository for extra visual representations and content***

This repository contains the implementation of an advanced information retrieval system designed to index and search HTML documents, utilizing both traditional and neural search methods. The system is built with Python and includes a web crawler, a TF-IDF indexer, neural indexing with Word2Vec and FAISS, and a Flask-based query processor.

## System Components

- `mycrawler.py`: A Scrapy-based web crawler that collects HTML documents from specified domains.
- `indexer.py`: A script that uses Scikit-Learn's TF-IDF to index documents for keyword-based searches.
- `text_processing.py`: A module that applies Word2Vec to capture document context and utilizes FAISS for indexing and retrieval.
- `app.py`: A Flask application that provides an API endpoint for processing search queries.

## Getting Started

### Prerequisites

Before running the system, ensure that you have Python 3.6+ installed, along with the following packages:

- Scrapy
- Scikit-Learn
- Gensim
- FAISS
- Flask
- NLTK

Install the required packages using `pip`:

```sh
pip install scrapy scikit-learn gensim faiss-cpu flask nltk
```

### Usage

#### 1. Running the Crawler

Navigate to the crawler directory and run:

```sh
scrapy crawl mycrawler
```

#### 2. Indexing Documents

After collecting the HTML documents, run the indexer to create the TF-IDF matrix:

```sh
python indexer.py
```

#### 3. Neural Indexing

To process documents with Word2Vec and create the FAISS index, execute:

```sh
python text_processing.py
```

#### 4. Starting the Query Processor

Launch the Flask application:

```sh
python app.py
```

Now you can make POST requests to `http://127.0.0.1:5001/search` to query the system.

## API Reference

The search API endpoint accepts POST requests with a JSON payload containing the search query. An example `curl` request:

```sh
curl -X POST http://127.0.0.1:5001/search \
-H "Content-Type: application/json" \
-d '{"query":"example search query", "top_k":5}'
```

## Testing

To run tests and evaluate the system, use the provided test scripts or utilize tools like `curl` and Postman to send requests to the API.

## Authors

- **Khiem Do** - *Initial work* - [dovudinhkhiem0905](https://github.com/dovudinhkhiem0905)


# Development of an Information Retrieval System with Neural Search Capabilities

**Author:** Khiem Do  
**Date:** 04/21/2024  
**Course:** CS 429 - Information Retrieval Spring 2024  
**Professor:** Prof. Panchal  

## I. Abstract

This report details the development of an advanced information retrieval system designed to index and search HTML documents. It integrates traditional search methods using Scikit-Learn's TF-IDF with neural search capabilities provided by Word2Vec and FAISS, all accessible via a Flask-based API. The system comprises several components, including a Scrapy-based web crawler, a Scikit-Learn indexer, a Word2Vec and FAISS module for semantic search, and a query processor in Flask.

## II. Introduction

The exponential growth of data on the internet necessitates efficient retrieval systems. This project aimed to build an information retrieval system that not only matches keywords but also understands context through neural search techniques.

## III. System Overview

The system is composed of three main components:

- **Web Crawler (`mycrawler.py`):** A Scrapy crawler that navigates specified domains and collects HTML documents.
- **Indexer (`indexer.py`):** Utilizes TF-IDF to index documents for quick keyword-based search.
- **Neural Indexer (`text_processing.py`):** Employs Word2Vec to understand document context and FAISS for fast indexing and retrieval.
- **Query Processor (`app.py`):** A Flask application providing an API endpoint for search queries, interfacing with both indices.

## IV. Methodology

The development was divided into distinct phases:

1. **Crawling:** The Scrapy crawler was set to target example domains, fetching HTML content and storing it locally.
2. **Indexing:**
   - **TF-IDF Indexing:** Extracted text from HTML documents to create a TF-IDF matrix.
   - **Neural Indexing:** Tokenized text was used to train a Word2Vec model, and resulting vectors were indexed using FAISS.

3. **Query Processing:**
   - Designed a Flask API to receive queries in JSON format.
   - Implemented handlers to use either the TF-IDF or neural index based on the query parameters.

## V. Implementation

Details of implementation are provided within the respective script files:

- Crawler Implementation in `mycrawler.py`
- Indexing Implementation in `indexer.py`
- Neural Indexing Implementation in `text_processing.py`
- Query Processor Implementation in `app.py`

## VI. Results and Discussion

### 1) Crawl Performance and Analysis

The Scrapy crawler's deployment and statistical outcomes are presented, including a summary of requests made and responses received, along with an analysis of findings and error analysis.

### 2) Visualization and Analysis of TF-IDF Scores

A bar chart visualizing the average TF-IDF scores for the top 20 terms, with a discussion on the implications for our indexing strategy and areas for improvement.

### 3) Visualization of Word2Vec Embeddings and FAISS Index Query Results

The visualization of Word2Vec embeddings using PCA and t-SNE, along with a discussion of the FAISS index query results, highlight the system's capabilities and areas needing further review.

### 4) Testing of Query Processor (app.py)

Documented tests verifying the functionality and error handling of the query processor, demonstrating its reliability and robust error handling.

## VII. Challenges

Challenges in optimizing the Word2Vec model, managing the sparsity of the TF-IDF matrix, and integrating FAISS with Word2Vec are discussed, along with the solutions implemented.

## VIII. Conclusion

A conclusion on the successful demonstration of the system's integration of traditional and neural search methods and its robust, reliable, and scalable nature.

## IX. Future Work

The future enhancements outlined include real-time indexing, broader domain crawling, improved NLP for query understanding, exploration of transformer-based models for semantic search, user experience enhancements, and performance optimization.




