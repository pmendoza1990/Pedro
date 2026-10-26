import streamlit as st
from PIL import Image

st.title("Mi Portafolio")

with st.sidebar:
    st.subheader("Aplicaciones")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

st.subheader("A continuación se presentan aplicaciones desarrolladas en IA, análisis de datos y aprendizaje automático.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sensores IoT sintéticos")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Esta aplicación permite visualizar y analizar sensores sintéticos de temperatura, humedad y presión en tiempo real, facilitando la exploración de datos de IoT.")
    url_ia = "https://d64fqn4eudfgfwmpt2tbsi.streamlit.app/"
    st.write(f"Sensores IoT: [Enlace]({url_ia})")

    st.subheader("Paralelismo")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("Aquí se explora el uso del paralelismo para optimizar procesos computacionales y mejorar la ejecución de tareas intensivas en ciencia de datos.")
    url = "https://appparalelismo-cjlmjmp8btjkfu27ydnvym.streamlit.app/"
    st.write(f"Paralelismo: [Enlace]({url})")

    st.subheader("Detector de anomalías")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Aplicación para identificar comportamientos anómalos en datos mediante técnicas de detección de outliers y análisis estadístico.")
    url = "https://detectoranomalias-8ks8khwvrfqsiusztiknyy.streamlit.app/"
    st.write(f"Detector de anomalías: [Enlace]({url})")

with col2:
    st.subheader("Predicción por regresión")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("Esta app muestra el uso de modelos de regresión para estimar valores continuos y entender relaciones entre variables.")
    url = "https://jseulzx2ydfcbdubhsgrgj.streamlit.app/"
    st.write(f"Regresión: [Enlace]({url})")

    st.subheader("Práctica 1")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("Práctica inicial orientada a la construcción y evaluación de soluciones analíticas básicas con enfoque educativo.")
    url = "https://practica1-sgufgmkxikkzdxcjcrs99o.streamlit.app/"
    st.write(f"Práctica 1: [Enlace]({url})")

    st.subheader("Pronóstico")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("Herramienta para generar predicciones a partir de series temporales y datos históricos, útil en planificación y toma de decisiones.")
    url = "https://pronostico-gttdnqn7thyz9kyxhujnbd.streamlit.app/"
    st.write(f"Pronóstico: [Enlace]({url})")

with col3:
    st.subheader("Regresión lineal")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("Se presenta una implementación de regresión lineal para modelar relaciones lineales y analizar la tendencia de variables numéricas.")
    url = "https://regresion-2jjqrbs2avzb3wvvf45lbr.streamlit.app/"
    st.write(f"Regresión lineal: [Enlace]({url})")

    st.subheader("Regresión logística")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Aplicación para clasificar resultados binarios mediante regresión logística, demostrando el uso del aprendizaje supervisado.")
    url = "https://regresion-logistica-67uy6bann2jjr3vdrmymnq.streamlit.app/"
    st.write(f"Regresión logística: [Enlace]({url})")

    st.subheader("Nivel de crecimiento")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Esta app ofrece una visualización y análisis del nivel de crecimiento asociado a indicadores clave, útil para monitoreo y evaluación.")
    url = "https://appnivelcornarepy-29rycltlbdp2dzs5v32xyl.streamlit.app/"
    st.write(f"Nivel de crecimiento: [Enlace]({url})")

st.subheader("Más aplicaciones")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Series de tiempo")
    st.write("Aplicación enfocada en el análisis y modelado de series temporales para detectar patrones, tendencia y comportamiento histórico.")
    url = "https://seriesdetiempo-djycav8uu5mi4tjqtceege.streamlit.app/"
    st.write(f"Series de tiempo: [Enlace]({url})")

with col5:
    st.subheader("Suelos")
    st.write("Herramienta para estudiar y visualizar datos relacionados con suelos, favoreciendo el análisis de propiedades y condiciones del terreno.")
    url = "https://suelos-lezugsqibpnrcablgafbbr.streamlit.app/"
    st.write(f"Suelos: [Enlace]({url})")

with col6:
    st.subheader("Tasa de aprendizaje")
    st.write("Se explora la influencia de la tasa de aprendizaje en el entrenamiento de modelos, mostrando cómo afecta la convergencia y el rendimiento.")
    url = "https://pmendoza1990-tasa-de-aprendizaje-app-gradient-otra-ob8021.streamlit.app/"
    st.write(f"Tasa de aprendizaje: [Enlace]({url})")
