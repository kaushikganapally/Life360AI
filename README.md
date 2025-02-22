Life360 AI

Overview

Life360 AI is an AI-powered assistant that helps users with health, wealth, and relationship advice through a multi-agent system. The project is built using CrewAI, FastAPI, and Mistral AI, with an iOS frontend developed in SwiftUI.

Features

Multi-Agent AI System: Uses CrewAI to coordinate AI agents specialized in different areas.

FastAPI Backend: Serves as the API layer to process user queries.

Mistral Model Integration: Utilizes the Mistral Large model for generating AI-driven insights.

iOS App with SwiftUI: Provides an intuitive user interface for interaction.

Seamless Communication: The frontend connects to the backend using RESTful API calls.

Tech Stack

Backend

FastAPI (for API management)

CrewAI (for multi-agent collaboration)

Mistral AI (LLM for response generation)

Python (core backend language)

Uvicorn (ASGI server)

dotenv (for environment variables)

Frontend

SwiftUI (iOS app development)

URLSession (for API calls)

Project Structure

Life360AI/
│── backend/
│   ├── main.py               # FastAPI application setup
│   ├── crew_ai_setup.py      # AI agents and task processing
│   ├── requirements.txt      # Dependencies
│── frontend/
│   ├── Life360AIApp.swift    # Main app entry point
│   ├── ContentView.swift     # UI with navigation and chat interface
│   ├── NetworkService.swift  # Handles API requests
│   ├── Message.swift         # Data model for chat messages
│── .gitignore                # Ignored files
│── README.md                 # Project documentation (this file)

Installation

Backend Setup

Clone the repository:

git clone https://github.com/kaushikganapally/Life360AI.git
cd Life360AI/backend

Set up a virtual environment and install dependencies:

python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
pip install -r requirements.txt

Create a .env file and add:

MISTRAL_API_KEY=your_api_key_here
MISTRAL_MODEL_NAME=mistral-large-latest

Run the FastAPI server:

uvicorn main:app --reload

Frontend Setup (iOS)

Open frontend/Life360AI.xcodeproj in Xcode.

Ensure your Mac has Xcode 15+ installed.

Build and run the app in the simulator.

Usage

Open the iOS app.

Enter a prompt related to health, wealth, or relationships.

The app sends the request to the backend.

CrewAI processes the query and returns a structured response.

The response is displayed in the chat interface.

API Endpoint

POST /ask-crew/

Description: Processes user prompts and returns AI-generated insights.

Request Body:

{
  "topic": "How can I improve my financial savings?"
}

Response:

{
  "response": "To improve your savings, consider tracking expenses and setting up automatic deposits."
}

Contribution

If you'd like to contribute:

Fork the repository.

Create a feature branch: git checkout -b feature-name

Commit changes using Conventional Commits.

Push and submit a pull request.

License

This project is licensed under the MIT License.

🚀 Life360 AI is under active development—stay tuned for updates!

