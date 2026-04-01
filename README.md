# AtlasShop Assist
Conversational AI assistant capable of answering customer questions using structured data and document-based retrieval (RAG).

## Overview

AtlasShop Assist is a simple conversational system built with FastAPI that simulates a customer support assistant.
It can:

- Retrieve customer information
- Check order status
- Verify refund details
- Answer questions using internal documentation

---

## How It Works

The system uses a simple orchestration layer to decide how to answer each question:

1. Detects if the message contains a **customer ID (CXXX)**
2. Detects if the message contains an **order ID (PXXXX)**
3. Otherwise, performs a **document search (RAG fallback)**

---

## Tech Stack

- Python 3.11
- FastAPI
- Pandas
- HTML + Bootstrap
- JavaScript (Fetch API)

---

## Project Structure
