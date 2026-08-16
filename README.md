# Medical Chatbot

A medical question-answering chatbot that uses Retrieval-Augmented Generation (RAG) to provide answers based on information extracted from a medical PDF/document.

## Project Overview

This project combines a Flask-based web application, semantic search, a vector database, and a generative AI model.

Instead of directly asking the AI model every question, the application first searches the stored medical knowledge for relevant information. The retrieved information is then provided to the AI model so that the response is grounded in the available medical content.

## How It Works

The project follows this workflow:

Medical PDF
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
ChromaDB
    ↓
User Question
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Document Chunks
    ↓
Prompt Construction
    ↓
Gemini
    ↓
Answer
    ↓
Chat Interface

## Main Features

- Medical question-answering chatbot
- PDF-based knowledge retrieval
- Text chunking for document processing
- Semantic search using embeddings
- Vector storage using ChromaDB
- Retrieval-Augmented Generation (RAG)
- Gemini-based response generation
- Flask backend
- Web-based chatbot interface
- AJAX-based communication between frontend and backend

## Technologies Used

### Backend
- Python
- Flask

### Artificial Intelligence
- Google Gemini
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- ChromaDB

### Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
- jQuery
- AJAX

## Project Structure

```text
Medical-Chatbot/
│
├── app.py
│
├── generate_embeddings.py
│
├── templates/
│   └── chat.html
│
├── static/
│   ├── style.css
│   └── doctor.png
│
├── data/
│   └── medical document/PDF
│
├── chroma_db/
│   └── vector database files
│
└── README.md
