# Information Retrieval System with Neural Search Capabilities

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

## Contributing

We welcome contributions to this project. Please fork the repository, make your changes, and submit a pull request for review.


## Authors

- **Khiem Do** - *Initial work* - [dovudinhkhiem0905](https://github.com/dovudinhkhiem0905)
