import streamlit as st
import requests
import base64

# Función para detectar texto usando Google Cloud Vision API
def detect_text_cloud_vision(image_data, api_key):
    """Detecta texto en una imagen usando Google Cloud Vision API."""
    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }

    # Codifica la imagen en base64
    encoded_image_data = base64.b64encode(image_data).decode("utf-8")

    # Construye la petición
    payload = {
        "requests": [{
            "image": {
                "content": encoded_image_data
            },
            "features": [{
                "type": "TEXT_DETECTION"
            }]
        }]
    }

    # Hace la petición a la API
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    # Extrae el texto detectado
    try:
        text = response_data["responses"][0]["textAnnotations"][0]["description"]
        return text
    except KeyError:
        return "No se detectó texto."

def main():
    st.title("Asistente de Lectura")
    uploaded_image = st.file_uploader("Sube tu imagen", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        image_data = uploaded_image.read()
        st.image(image_data, caption="Imagen cargada.", use_column_width=True)

        # Aquí es donde llamas a la función de detección de texto
        # TODO: Reemplaza con tu clave de API real o usa st.secrets si estás en Streamlit Sharing
        api_key = "YOUR_GOOGLE_CLOUD_API_KEY"
        detected_text = detect_text_cloud_vision(image_data, api_key)
        
        # Mostrar el texto detectado
        st.write("Texto detectado:")
        st.write(detected_text)

if __name__ == "__main__":
    main()
