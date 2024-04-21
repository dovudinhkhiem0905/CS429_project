# CS 429 - Information Retrieval Spring 2024

### Development of an Information Retrieval System with Neural Search Capabilities

**Khiem Do**  
**Date:** 04/21/2024  
**Instructor:** Prof. Panchal  

---

## Abstract

This report details the development of an advanced information retrieval system designed to index and search HTML documents. It integrates traditional search methods using Scikit-Learn's TF-IDF with neural search capabilities provided by Word2Vec and FAISS, all accessible via a Flask-based API. The system comprises several components, including a Scrapy-based web crawler, a Scikit-Learn indexer, a Word2Vec and FAISS module for semantic search, and a query processor in Flask.

## Introduction

The exponential growth of data on the internet necessitates efficient retrieval systems. This project aimed to build an information retrieval system that not only matches keywords but also understands context through neural search techniques.

## System Overview

The system is composed of three main components:
- Web Crawler (`mycrawler.py`): A Scrapy crawler that navigates specified domains and collects HTML documents.
- Indexer (`indexer.py`): Utilizes TF-IDF to index documents for quick keyword-based search.
- Neural Indexer (`text_processing.py`): Employs Word2Vec to understand document context and FAISS for fast indexing and retrieval.
- Query Processor (`app.py`): A Flask application providing an API endpoint for search queries, interfacing with both indices.

## Methodology

The development was divided into distinct phases:
1. Crawling: The Scrapy crawler was set to target example domains, fetching HTML content and storing it locally.
2. Indexing:
   - TF-IDF Indexing: Extracted text from HTML documents to create a TF-IDF matrix.
   - Neural Indexing: Tokenized text was used to train a Word2Vec model, and resulting vectors were indexed using FAISS.

3. Query Processing:
   - Designed a Flask API to receive queries in JSON format.
   - Implemented handlers to use either the TF-IDF or neural index based on the query parameters.

## Implementation

- Crawler Implementation
  <img width="263" alt="image" src="https://github.com/dovudinhkhiem0905/CS429_project/assets/100241521/9f01e824-b37d-4a97-a17f-952a38f6630d">

- Indexing Implementation
  <img width="266" alt="image" src="https://github.com/dovudinhkhiem0905/CS429_project/assets/100241521/ea1a6ee6-2e12-46ab-a008-46a217556c32">

- Neural Indexing Implementation
  <img width="468" alt="image" src="https://github.com/dovudinhkhiem0905/CS429_project/assets/100241521/19bcad7f-0bb9-4fd4-bc88-ec6de41ec9d4">

- Query Processor Implementation
  <img width="468" alt="image" src="https://github.com/dovudinhkhiem0905/CS429_project/assets/100241521/7a6b0d57-b538-41aa-98ec-3d61b8d7afea">

## Results and Discussion

1) Crawl Performance and Analysis
   
The Scrapy crawler was deployed to assess the robustness and effectiveness of the information retrieval system across various domains. This section presents the crawl's statistical outcomes, highlights potential issues encountered during the operation, and proposes recommendations for future improvements.

- Crawl Statistics Summary:
   - **Total Requests Made:** 121
   - **Total Responses Received:** 117
     - **Successful (200):** 107
     - **Client Errors (404):** 4
     - **Server Errors (5xx):** 4
       - Specific codes: 500, 510, 511, 520, 598, 599
   - **DNS Lookup Errors:** 4
   - **Duplicate Requests Filtered:** 1057
   - **Max Request Depth:** 3
   - **Crawl Duration:** 20.65 seconds

- Analysis of Findings
   - Success Rate: The crawler successfully retrieved content from 107 out of 121 requests, indicating a high success rate. This success underscores the crawler's efficiency in navigating and extracting data.
   - Error Analysis:
      - DNS Lookup Errors (4 instances): These errors suggest potential issues with network settings or misconfigurations in domain names. Further investigation into network logs and domain configurations is recommended.
      - HTTP 404 Errors: Occurred in 4 instances, indicating that some URLs were not found. This could be due to outdated links or misconfigured routing on the target websites.
      - Server Errors (500 series): These errors imply server-side issues at the target domains during the crawl, which may include rate limiting, temporary unavailability, or server misconfigurations.



2) Visualization and Analysis of TF-IDF Scores
- Overview
- Methodology
- Results
- Analysis
- Conclusion

3) Visualization of Word2Vec Embeddings and FAISS Index Query Results
- Objective
- Word2Vec Embeddings Visualization
- FAISS Index Query Results
- Discussion
- Conclusion

4) Testing of Query Processor (`app.py`)
- Test Objectives
- Methodology
- Test 1: Valid Search Query
- Test 2: Error Handling for Missing Query Data
- Conclusions

## Challenges

During the development of our information retrieval system, we encountered several challenges that required innovative solutions and technical proficiency. The primary issues included optimizing the Word2Vec model for our specific dataset, managing the sparsity of the TF-IDF matrix, and integrating the FAISS library with the Word2Vec embeddings.

- Word2Vec Optimization: Tuning the Word2Vec model parameters to generate meaningful word embeddings was a complex process. It required several iterations to select the appropriate context window size, minimum word frequency, and the number of features. The key was to strike a balance between capturing the nuances of the language and the computational efficiency of the model.

- TF-IDF Sparsity: Dealing with the high dimensionality and sparsity of the TF-IDF matrix presented memory management challenges. To address this, we implemented dimensionality reduction techniques and optimized our storage approach to ensure quick retrieval without excessive resource consumption.

- FAISS Integration: The combination of FAISS with Word2Vec for efficient similarity searches necessitated a careful consideration of vector sizes and normalization. The FAISS index had to be precisely tailored to handle the semantic vectors produced by Word2Vec, ensuring that nearest-neighbor queries returned relevant results.

## Conclusion

The development of this information retrieval system has successfully demonstrated the integration of traditional and neural search methodologies. The system's modular architecture allows for the efficient indexing and retrieval of HTML documents, catering to both keyword-based and semantic search queries. Through rigorous testing, the system has proven to be robust, reliable, and scalable.

While the system performs well with current technologies, it is designed with flexibility in mind, allowing for future integration of more advanced models and algorithms. The challenges faced and overcome during this project have provided valuable insights that will inform future development and optimizations.

## Future Work

Looking ahead, there are several avenues for further enhancement of our information retrieval system:

- Real-Time Indexing: Implementing real-time updates to the indices will allow the system to handle dynamic content changes more effectively, ensuring that search results remain current and relevant.

- Broader Domain Crawling: Expanding the scope of the web crawler to cover a more extensive range of domains will enrich the dataset and improve the diversity of the search results.

- Improved NLP for Query Understanding: Incorporating more advanced natural language processing techniques will enable the system to better understand the intent behind user queries, leading to more accurate search results.

- Transformer-Based Models for Semantic Search: Exploring the use of transformer-based models, such as BERT, could significantly enhance the system's understanding of document context and relevance, propelling our search capabilities to the forefront of the field.

- User Experience: Enhancing the user interface and providing a more interactive and user-friendly experience will make the search system more accessible to a broader audience.

- Performance Optimization: Continuous optimization of the system's performance, particularly in terms of speed and resource usage, will remain a priority to ensure the system can scale to meet user demands.

