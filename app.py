import streamlit as st
from textblob import TextBlob
from gtts import gTTS
import os

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.01:
        return "Positivo"
    elif analysis.sentiment.polarity < -0.01:
        return "Negativo"
    else:
        return "Neutro"

def text_to_speech(text):
    temp_file = "temp_audio.mp3"
    tts = gTTS(text=text, lang='es')
    tts.save(temp_file)
    return temp_file

def main():
    st.title("Análisis de Sentimiento y Conversión a Audio")

    user_input = st.text_area("Escribe un texto para analizar:", key="text_area_key")
    if user_input:
        sentiment = analyze_sentiment(user_input)
        st.write(f"Sentimiento del texto: {sentiment}")

        temp_audio_file = text_to_speech(user_input)  # Ahora se convierte el texto del usuario a audio
        st.audio(temp_audio_file, format='audio/mp3')

        # Limpieza: eliminar el archivo temporal después de usarlo
        os.remove(temp_audio_file)

if __name__ == "__main__":
    main()



