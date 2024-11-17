**<span style="font-size: 15px;">Authors:</span>** *João Fonseca*  *|*  *Gabriel Pinto* <br>
**<span style="font-size: 15px;">Date:</span>** *9 de Novembro de 2024*

---

# Semantic Search Implementation—BTL News

This file implements semantic search capabilities for the **BTL News** legal news portal, enabling users to find relevant documents based on semantically-informed queries. The search mechanism leverages embeddings to represent the text of documents as dense vectors, allowing for similarity-based matching between user queries and the stored documents.

## Project Structure

The project is organized into directories to facilitate modularization and maintainability:

**<span style="font-size: 20px;">semantic_search/</span>**  
├── **<span style="font-size: 16px;">main.py</span>**  
├── **<span style="font-size: 16px;">database/</span>**  
│   ├── **<span style="font-size: 13px;">\_\_init\_\_.py</span>**  
│   ├── **<span style="font-size: 13px;">config.py</span>**  
│   ├── **<span style="font-size: 13px;">models.py</span>**  
├── **<span style="font-size: 16px;">embeddings/</span>**  
│   ├── **<span style="font-size: 13px;">\_\_init\_\_.py</span>**  
│   ├── **<span style="font-size: 13px;">generate_embeddings.py</span>**  
│   ├── **<span style="font-size: 13px;">search.py</span>**  
├── **<span style="font-size: 16px;">requirements.txt</span>**
---
# File Descriptions

## Main Program File

- **`main.py`**: The primary script to run the program, which:
  1. Generates embeddings for documents and saves them to a file for efficient future access.
  2. Conducts a test semantic query, displaying the most relevant results.

## Database Directory

This directory contains all files related to database management.

- **`__init__.py`**: Initializes the `database` module, allowing it to be imported as a package.
- **`config.py`**: Manages the database connection settings using SQLAlchemy. This file sets the database URI and creates a session for accessing the database.
- **`models.py`**: Defines SQLAlchemy ORM classes that map to the database tables. This file facilitates data manipulation with classes representing the tables `dreapp_document`, `dreapp_documenttext`, and `dreapp_document_connects_to`.

## Embeddings Directory

This directory includes all scripts related to generating and managing document embeddings for semantic search.

- **`__init__.py`**: Initializes the `embeddings` module.
- **`generate_embeddings.py`**: Generates and saves embeddings for the documents. This script loads a pre-trained model to process document text into embeddings, which are stored in a `document_embeddings.pkl` file for future search operations.
- **`search.py`**: Contains the semantic search function, which performs similarity matching between the user query embedding and document embeddings, returning the most relevant documents.

## Dependencies

- **`requirements.txt`**: Lists the project’s required libraries, including:
  - `sqlalchemy`: For database management.
  - `transformers` and `sentence-transformers`: For generating embeddings.
  - `torch`: A deep learning framework required by `sentence-transformers`.

---

# Usage Instructions

1. **Install Dependencies**:
   - Install all necessary dependencies listed in `requirements.txt` by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Database Configuration**:
   - Configure the database URI in `database/config.py` to connect to the desired database.

3. **Generate Document Embeddings**:
   - Run `main.py` to generate and store embeddings for all documents. This step processes each document in the database, creating the `document_embeddings.pkl` file needed for semantic search:
     ```bash
     python main.py
     ```

4. **Perform Semantic Search**:
   - With embeddings generated and stored, `main.py` also performs a test semantic search, displaying the most relevant documents based on the defined query.

# Example Execution

To generate embeddings and execute a sample query, run:

```bash
python main.py
