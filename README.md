# Generative AI Practice

This repository contains practice scripts for working with Generative AI models using the Mistral API.

## Files

### 1. `mistral_first.py`
This script demonstrates how to interact with the Mistral API to generate responses based on a given prompt. It sends a POST request to the API and handles the server's response.

#### Features:
- Sends a prompt to the Mistral API.
- Handles JSON responses from the server.
- Includes error handling for invalid responses or missing keys.

#### Usage:
1. Ensure the Mistral API server is running locally on `http://localhost:11434`.
2. Run the script:
   ```bash
   python mistral_first.py

   