import streamlit as st
import requests
import base64
from io import BytesIO

# Función para detectar el sentimiento del texto usando la API de Google Cloud Natural Language
def analyze_sentiment(text, api_key):
    url = f"https://language.googleapis.com/v1/documents:analyzeSentiment?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": text
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    sentiment_data = response.json()

    try:
        score = sentiment_data['documentSentiment']['score']
        if score >= 0.25:
            return "Positivo"
        elif score <= -0.25:
            return "Negativo"
        else:
            return "Neutro"
    except KeyError:
        return "No se pudo determinar el sentimiento."

# Función para convertir texto a audio usando la API de Google Cloud Text-to-Speech
def text_to_speech(text, api_key):
    url = f"https://texttospeech.googleapis.com/v1/text:speak?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "input": {"text": text},
        "voice": {"languageCode": "es-ES", "ssmlGender": "NEUTRAL"},
        "audioConfig": {"audioEncoding": "MP3"}
    }

    response = requests.post(url, headers=headers, json=payload)
    audio_data = response.json()

    try:
        audio_content = audio_data['audioContent']
        return base64.b64decode(audio_content)
    except KeyError:
        return None

def main():
    st.title("Análisis de Sentimiento y Conversión a Audio")

    user_input = st.text_area("Escribe un texto para analizar:")
    if user_input:
        # Aquí es donde llamas a la función de detección de sentimiento
        api_key = "YOUR_GOOGLE_CLOUD_API_KEY"
        sentiment = analyze_sentiment(user_input, api_key)
        st.write(f"Sentimiento del texto: {sentiment}")

        audio_data = text_to_speech(user_input, api_key)
        if audio_data:
            audio_stream = BytesIO(audio_data)
            st.audio(audio_stream, format='audio/mp3')

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
