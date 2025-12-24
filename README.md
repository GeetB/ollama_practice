# Generative AI Practice

This repository contains practice scripts and a web-based chatbot interface for working with Generative AI models using the Mistral API.

---

## Project Structure

### Files
1. **`mistral_first.py`**:
   - Demonstrates how to interact with the Mistral API to generate responses based on a given prompt.
   - Handles JSON responses and includes error handling for invalid responses or missing keys.

2. **`mistral_second.py`**:
   - Extends the functionality of `mistral_first.py` with additional features such as streaming responses and batch processing.

3. **`ai_chatbot_ollama/`**:
   - Contains the FastAPI-based chatbot application, including:
     - `app.py`: The backend server for handling requests and communicating with the Mistral API.
     - `static/`: Frontend files (`index.html`, `style.css`, `script.js`) for the chatbot interface.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)
- FastAPI and Uvicorn for the backend
- `requests` library for API communication

### Steps to Set Up the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ollama_practice
2. **Create a Virtual Environment (Optional but Recommended)**:
   python3 -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
3. **Install Required Libraries: Install the dependencies listed below**:
   pip install fastapi uvicorn requests
4. **Run the FastAPI Server: Navigate to the ai_chatbot_ollama directory and start the server**:
   cd ai_chatbot_ollama
   uvicorn app:app --reload
5. **Access the Chatbot Interface: Open your browser and navigate to**:
   http://127.0.0.1:8000
6. **Test the Chatbot**:
   Type a message in the input field and click "Send."
   The chatbot will display the AI's response.

**Required Python Libraries**
Here’s a list of the Python libraries used in this project:

1. FastAPI: For building the backend API.
2. Uvicorn: ASGI server for running the FastAPI application.
3. Requests: For making HTTP requests to the Mistral API.

**To install all dependencies at once, you can use the following command**:

pip install -r requirements.txt

Example requirements.txt File
If you want to create a requirements.txt file for the project, include the following:

**Notes**
Ensure the Mistral API server is running locally on http://localhost:11434 before starting the chatbot.
Update the OLLAMA_URL in app.py if the API server is hosted on a different URL or port.
License
This project is for educational purposes only.


