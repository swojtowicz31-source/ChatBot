# AI Chatbot + Dashboard
A simple **Streamlit** application for chatting with AI models via the **OpenRouter API**. It stores conversation history in a CSV file and displays basic analytics on a dashboard.
## Features
- Chat with multiple AI models (Mistral, GPT-4, Claude)
- Real-time responses from the selected model
- Saves conversation history to `history.csv`
- Dashboard with recent conversations and most frequently asked questions (bar chart)
## Installation
1. Clone the repository:

cd ai-chatbot-dashboard
Install dependencies:

pip install streamlit pandas matplotlib requests
Set your OpenRouter API key in chat_logic.py:
python
OPENROUTER_API_KEY = "YOUR_API_KEY"
Run the app:

streamlit run app.py
Open in browser at http://localhost:8501
File Structure

├── app.py            # Streamlit UI
├── chat_logic.py     # Functions for API calls and history handling
├── history.csv       # Saved conversation history
└── README.md

Requirements
Python 3.8+
Streamlit
Pandas
Matplotlib
Requests
