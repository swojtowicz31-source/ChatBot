import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from chat_logic import get_ai_response, save_interaction, load_history

st.set_page_config(page_title="AI Chatbot + Dashboard", layout="wide")
st.title(" AI Chatbot + Dashboard")

# Panel z rozmową
st.header(" Rozmowa z AI")
user_input = st.text_input("Zadaj pytanie:", key="input")

if st.button("Wyślij"):
    if user_input:
        with st.spinner("Generowanie odpowiedzi..."):
            response = get_ai_response(user_input)
            save_interaction(user_input, response)
            st.success("Odpowiedź AI:")
            st.markdown(f"**{response}**")

# Panel z historią
st.header(" Historia rozmów")

history = load_history()
if not history.empty:
    st.dataframe(history.tail(10), use_container_width=True)

    # Analiza zapytań
    st.subheader(" Najczęściej zadawane pytania (top 5)")
    top_questions = history['question'].value_counts().nlargest(5)
    
    fig, ax = plt.subplots()
    top_questions.plot(kind='barh', ax=ax, color="skyblue")
    ax.set_xlabel("Liczba wystąpień")
    ax.set_ylabel("Pytania")
    ax.invert_yaxis()
    st.pyplot(fig)
else:
    st.info("Brak zapisanej historii.")
# Panel z dashboardem