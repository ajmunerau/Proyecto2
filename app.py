import streamlit as st
from textblob import TextBlob
from gtts import gTTS
from io import BytesIO

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0.1:
        return "Positivo"
    elif analysis.sentiment.polarity < -0.1:
        return "Negativo"
    else:
        return "Neutro"

def text_to_speech(text):
    tts = gTTS(text=text, lang='es')
    audio_data = BytesIO()
    tts.save(audio_data)
    audio_data.seek(0)
    return audio_data

def main():
    st.title("Análisis de Sentimiento y Conversión a Audio")

    user_input = st.text_area("Escribe un texto para analizar:", key="text_area_key")
    if user_input:
        sentiment = analyze_sentiment(user_input)
        st.write(f"Sentimiento del texto: {sentiment}")

        if sentiment != "Neutro":
            audio_data = text_to_speech(user_input)
            st.audio(audio_data, format='audio/mp3')
        else:
            st.write("El texto es neutro, por lo tanto, no se generará audio.")

if __name__ == "__main__":
    main()
