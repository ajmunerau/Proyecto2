import streamlit as st
from PIL import Image
import pytesseract
import pyttsx3

def main():
    st.title("Asistente de Lectura")

    uploaded_file = st.file_uploader("Carga una imagen con texto", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen cargada", use_column_width=True)
        st.write("Detectando texto...")
        
        # Extraer texto de la imagen
        detected_text = pytesseract.image_to_string(image)
        
        if detected_text:
            st.subheader("Texto detectado:")
            st.write(detected_text)

            # Reproducir el texto detectado
            if st.button("Reproducir Texto"):
                engine = pyttsx3.init()
                engine.say(detected_text)
                engine.runAndWait()
        else:
            st.write("No se detectó ningún texto en la imagen.")

if __name__ == "__main__":
    main()
