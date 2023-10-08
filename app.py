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

def translate_text(text, target_language='en'):
    blob = TextBlob(text)
    try:
        translated_text = blob.translate(to=target_language)
        return str(translated_text)
    except:
        return text  # If translation fails, return the original text

def main():
    st.markdown("<h1 style='text-align: center; color: blue;'>Asistente de Análisis de Sentimiento y Traducción</h1>", unsafe_allow_html=True)
    
    st.markdown("## 🎤 Ingresa tu texto")
    user_input = st.text_area("")
    
    # Option to translate the text
    st.markdown("## 🌍 Traducir texto")
    translation_target = st.selectbox("Traducir a:", ["No traducir", "Inglés", "Español", "Francés", "Alemán", "Italiano", "Chino"])
    language_mapping = {"Inglés": "en", "Español": "es", "Francés": "fr", "Alemán": "de", "Italiano": "it", "Chino": "zh-CN"}
    
    if translation_target != "No traducir":
        user_input_translated = translate_text(user_input, language_mapping[translation_target])
        st.write(f"Texto traducido: {user_input_translated}")
    else:
        user_input_translated = user_input
    
    if st.button("Analizar"):
        st.markdown("## 📊 Resultados")
        sentiment = analyze_sentiment(user_input_translated)
        st.write(f"El sentimiento del texto es: {sentiment}")
        
        st.markdown("## 🎧 Reproducir texto")
        audio_file = text_to_speech(user_input_translated)
        audio_bytes = open(audio_file, 'rb').read()
        st.audio(audio_bytes, format="audio/mp3")

    st.write("---")
    st.sidebar.title("Instrucciones:")
    st.sidebar.markdown("1. Ingresa un texto.")
    st.sidebar.markdown("2. Opcional: Elige un idioma para traducir el texto.")
    st.sidebar.markdown("3. Haz clic en 'Analizar' para determinar el sentimiento.")
    st.sidebar.markdown("4. Escucha el audio con el texto (traducido si se eligió).")

if __name__ == "__main__":
    main()

