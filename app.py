import streamlit as st
from utils import generate_image, classify_image

def main():
    st.title("Aplicación de Generación y Clasificación de Imágenes")

    st.sidebar.header("Sección de Generación de Imágenes")
    user_input_generation = st.sidebar.text_input("Ingrese solicitud de generación de imágenes:")

    st.sidebar.header("Sección de Clasificación de Imágenes")
    uploaded_file = st.sidebar.file_uploader("Cargar imagen para clasificación:")

    if user_input_generation:
        generated_image = generate_image(user_input_generation)
        st.image(generated_image, caption="Imagen generada")

    if uploaded_file is not None:
        classified_label = classify_image(uploaded_file)
        st.write("Clasificación de imagen:", classified_label)

if __name__ == "__main__":
    main()
