import requests
import streamlit as st
import pandas as pd
from datetime import datetime


selected_model = st.selectbox(
    "Wybierz model AI:",
    ["mistralai/mistral-7b-instruct", "openai/gpt-4", "anthropic/claude-3-opus"]
)

# Twój klucz OpenRouter API:
OPENROUTER_API_KEY = "sk..."    # Upewnij się, że masz poprawny klucz API

# Plik CSV do zapisu historii
HISTORY_FILE = "history.csv"

def get_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Jesteś pomocnym asystentem AI."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Błąd OpenRouter API: {str(e)}"

def save_interaction(user_input, ai_response):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = pd.DataFrame([[now, user_input, ai_response]], columns=["timestamp", "question", "response"])
    try:
        df = pd.read_csv(HISTORY_FILE)
        df = pd.concat([df, new_row], ignore_index=True)
    except FileNotFoundError:
        df = new_row
    df.to_csv(HISTORY_FILE, index=False)

def load_history():
    try:
        return pd.read_csv(HISTORY_FILE)
    except FileNotFoundError:
        # Plik nie istnieje - zwróć pusty DataFrame z kolumnami
        return pd.DataFrame(columns=["timestamp", "question", "response"])
    except pd.errors.EmptyDataError:
        # Plik jest pusty - też zwróć pusty DataFrame
        return pd.DataFrame(columns=["timestamp", "question", "response"])
