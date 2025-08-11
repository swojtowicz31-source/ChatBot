# AI Chatbot + Dashboard

A simple **Streamlit** application for chatting with AI models via the **OpenRouter API**.  
It stores conversation history in a CSV file and displays basic analytics on a dashboard.

---

## Features

- Chat with multiple AI models (Mistral, GPT-4, Claude)  
- Real-time responses from the selected model  
- Saves conversation history to `history.csv`  
- Dashboard with recent conversations and most frequently asked questions (bar chart)  

---

## Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd ai-chatbot-dashboard
pip install streamlit pandas matplotlib requests
Edit the file chat_logic.py and set your API key:
OPENROUTER_API_KEY = "YOUR_API_KEY"

Run the app:
streamlit run app.py
Open in your browser:
Navigate to http://localhost:8501

Requirements
Python 3.8 or higher
Streamlit
Pandas
Matplotlib
Requests
