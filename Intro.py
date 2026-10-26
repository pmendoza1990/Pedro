import streamlit as st
from PIL import Image

st.title("Mi Portafolio")
st.caption("Inteligencia artificial, analítica de datos y aprendizaje automático")

with st.sidebar:
    st.subheader("Portafolio")
    st.write(
        "Exploro soluciones de IA para la toma de decisiones, monitoreo de datos, "
        "predicción y optimización de modelos aplicados a problemas reales."
    )

st.subheader("Proyectos y aplicaciones")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sensores IoT sintéticos")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write(
        "Aplicación para monitorear variables como temperatura, humedad y presión en tiempo real, "
        "ideal para la visualización de datos operativos y el análisis de sistemas IoT."
    )
    url = "https://d64fqn4eudfgfwmpt2tbsi.streamlit.app/"
    st.write(f"Sensores IoT: [Enlace]({url})")

    st.subheader("Paralelismo")
    image = Image.open('data_analisis.png')
    st.image(image, width=200)
    st.write(
        "Proyecto enfocado en la optimización computacional mediante paralelismo, mostrando cómo se "
        "pueden acelerar tareas intensivas de cálculo y análisis de datos."
    )
    url = "https://appparalelismo-cjlmjmp8btjkfu27ydnvym.streamlit.app/"
    st.write(f"Paralelismo: [Enlace]({url})")

    st.subheader("Detector de anomalías")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write(
        "Herramienta para identificar patrones fuera de lo normal en conjuntos de datos, útil en "
        "monitorización, detección temprana y alertas basadas en comportamiento anómalo."
    )
    url = "https://detectoranomalias-8ks8khwvrfqsiusztiknyy.streamlit.app/"
    st.write(f"Detector de anomalías: [Enlace]({url})")

with col2:
    st.subheader("Modelos de regresión")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write(
        "Aplicación centrada en la regresión como técnica predictiva para estimar variables numéricas "
        "y comprender relaciones entre diferentes indicadores."
    )
    url = "https://jseulzx2ydfcbdubhsgrgj.streamlit.app/"
    st.write(f"Modelos de regresión: [Enlace]({url})")

    st.subheader("Práctica 1")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write(
        "Actividad introductoria para explorar fundamentos de análisis de datos, visualización y "
        "aplicación de conceptos básicos de ciencia de datos en un entorno práctico."
    )
    url = "https://practica1-sgufgmkxikkzdxcjcrs99o.streamlit.app/"
    st.write(f"Práctica 1: [Enlace]({url})")

    st.subheader("Pronóstico")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write(
        "Proyecto para modelar series temporales y generar predicciones a partir de datos históricos, "
        "permitiendo anticipar tendencias y apoyar la toma de decisiones."
    )
    url = "https://pronostico-gttdnqn7thyz9kyxhujnbd.streamlit.app/"
    st.write(f"Pronóstico: [Enlace]({url})")

with col3:
    st.subheader("Regresión lineal")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write(
        "Modelo de regresión lineal orientado a identificar patrones lineales entre variables y "
        "describir comportamientos cuantitativos a partir de datos observados."
    )
    url = "https://regresion-2jjqrbs2avzb3wvvf45lbr.streamlit.app/"
    st.write(f"Regresión lineal: [Enlace]({url})")

    st.subheader("Regresión logística")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write(
        "Aplicación para modelar clasificación binaria mediante regresión logística, útil en escenarios "
        "de evaluación de riesgo, decisiones y categorización de eventos."
    )
    url = "https://regresion-logistica-67uy6bann2jjr3vdrmymnq.streamlit.app/"
    st.write(f"Regresión logística: [Enlace]({url})")

    st.subheader("Nivel de crecimiento")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write(
        "Análisis del crecimiento y evolución de indicadores clave, pensado para visualizar tendencias "
        "y evaluar métricas de rendimiento en contextos empresariales o de investigación."
    )
    url = "https://appnivelcornarepy-29rycltlbdp2dzs5v32xyl.streamlit.app/"
    st.write(f"Nivel de crecimiento: [Enlace]({url})")

st.subheader("Más proyectos")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Series de tiempo")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write(
        "Análisis de series temporales para detectar patrones, comportamientos cíclicos y tendencias "
        "que permiten pronosticar eventos futuros con mayor precisión."
    )
    url = "https://seriesdetiempo-djycav8uu5mi4tjqtceege.streamlit.app/"
    st.write(f"Series de tiempo: [Enlace]({url})")

with col5:
    st.subheader("Suelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write(
        "Aplicación orientada al análisis de datos de suelos y variables del terreno, con enfoque en la "
        "exploración y evaluación de condiciones relevantes para toma de decisiones técnicas."
    )
    url = "https://suelos-lezugsqibpnrcablgafbbr.streamlit.app/"
    st.write(f"Suelos: [Enlace]({url})")

with col6:
    st.subheader("Tasa de aprendizaje")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=200)
    st.write(
        "Proyecto dedicado a evaluar la influencia de la tasa de aprendizaje en el entrenamiento de modelos, "
        "mostrando cómo este hiperparámetro impacta convergencia y desempeño final."
    )
    url = "https://pmendoza1990-tasa-de-aprendizaje-app-gradient-otra-ob8021.streamlit.app/"
    st.write(f"Tasa de aprendizaje: [Enlace]({url})")

st.markdown("---")
st.caption("Portfolio de soluciones basadas en IA, analítica avanzada y aprendizaje automático.")
