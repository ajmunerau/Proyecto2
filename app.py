import streamlit as st
from gtts import gTTS
from textblob import TextBlob

# Cambiar el fondo y otros estilos
st.markdown(
    """
    <style>
    body {
        background-color: #e6f7ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def text_to_speech(text):
    temp_file = "temp_audio.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(temp_file)
    return temp_file

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.5:
        return "😃 Muy positivo"
    elif analysis.sentiment.polarity > 0:
        return "🙂 Positivo"
    elif analysis.sentiment.polarity == 0:
        return "😐 Neutral"
    elif analysis.sentiment.polarity > -0.5:
        return "🙁 Negativo"
    else:
        return "☹️ Muy negativo"

def main():
    st.markdown("<h1 style='text-align: center; color: blue;'>Asistente de Análisis de Sentimiento</h1>", unsafe_allow_html=True)
    
    st.markdown("## 🎤 Ingresa tu texto")
    user_input = st.text_area("")
    
    if st.button("Analizar"):
        st.markdown("## 📊 Resultados")
        sentiment = analyze_sentiment(user_input)
        st.write(f"El sentimiento del texto es: {sentiment}")
        
        st.markdown("## 🎧 Reproducir texto")
        audio_file = text_to_speech(user_input)
        audio_bytes = open(audio_file, 'rb').read()
        st.audio(audio_bytes, format="audio/mp3")

    st.write("---")
    st.sidebar.title("Instrucciones:")
    st.sidebar.markdown("1. Ingresa un texto en inglés.")
    st.sidebar.markdown("2. Haz clic en 'Analizar' para determinar el sentimiento.")
    st.sidebar.markdown("3. Escucha el audio con el texto ingresado.")

if __name__ == "__main__":
    main()


