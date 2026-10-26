import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mi Portafolio", page_icon="🤖", layout="wide")

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .title {
        font-size: 2.7rem;
        font-weight: 700;
        color: #1f4e79;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        font-size: 1.15rem;
        color: #4a4a4a;
        margin-bottom: 1.5rem;
    }
    .section-title {
        font-size: 1.7rem;
        font-weight: 700;
        color: #1f4e79;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .caption {
        color: #5b5b5b;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Mi Portafolio</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Inteligencia artificial, analítica de datos y aprendizaje automático</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("Perfil")
    st.write(
        "Desarrollo soluciones de IA para apoyar la toma de decisiones, análisis predictivo, "
        "modelado estadístico y optimización de procesos con datos reales."
    )
    st.markdown("---")
    st.subheader("Áreas")
    st.write("- IoT y sensores")
    st.write("- Machine learning")
    st.write("- Series de tiempo")
    st.write("- Regresión y clasificación")
    st.write("- Análisis de datos")

st.markdown('<div class="section-title">Proyectos y aplicaciones</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Sensores IoT sintéticos",
        "image": "data_analisis.png",
        "description": "Aplicación para monitorear variables como temperatura, humedad y presión en tiempo real, ideal para la visualización de datos operativos y análisis de sistemas IoT.",
        "url": "https://d64fqn4eudfgfwmpt2tbsi.streamlit.app/",
    },
    {
        "title": "Paralelismo",
        "image": "audio_to_txt.png",
        "description": "Proyecto enfocado en la optimización computacional mediante paralelismo, mostrando cómo acelerar tareas intensivas de cálculo y análisis de datos.",
        "url": "https://appparalelismo-cjlmjmp8btjkfu27ydnvym.streamlit.app/",
    },
    {
        "title": "Detector de anomalías",
        "image": "txt_to_audio2.png",
        "description": "Herramienta para identificar patrones fuera de lo normal en conjuntos de datos, útil en detección temprana y análisis de comportamiento anómalo.",
        "url": "https://detectoranomalias-8ks8khwvrfqsiusztiknyy.streamlit.app/",
    },
    {
        "title": "Modelos de regresión",
        "image": "OIG3.png",
        "description": "Aplicación centrada en la regresión como técnica predictiva para estimar variables numéricas y comprender relaciones entre indicadores.",
        "url": "https://jseulzx2ydfcbdubhsgrgj.streamlit.app/",
    },
    {
        "title": "Práctica 1",
        "image": "audio_to_txt.png",
        "description": "Actividad introductoria para explorar fundamentos de análisis de datos, visualización y aplicación de conceptos básicos de ciencia de datos.",
        "url": "https://practica1-sgufgmkxikkzdxcjcrs99o.streamlit.app/",
    },
    {
        "title": "Pronóstico",
        "image": "OIG2.jpg",
        "description": "Proyecto para modelar series temporales y generar predicciones a partir de datos históricos, permitiendo anticipar tendencias y apoyar decisiones.",
        "url": "https://pronostico-gttdnqn7thyz9kyxhujnbd.streamlit.app/",
    },
    {
        "title": "Regresión lineal",
        "image": "Chat_pdf.png",
        "description": "Modelo de regresión lineal orientado a identificar patrones entre variables y describir comportamientos cuantitativos a partir de datos observados.",
        "url": "https://regresion-2jjqrbs2avzb3wvvf45lbr.streamlit.app/",
    },
    {
        "title": "Regresión logística",
        "image": "txt_to_audio.png",
        "description": "Aplicación para modelar clasificación binaria mediante regresión logística, útil en evaluaciones de riesgo y categorización de eventos.",
        "url": "https://regresion-logistica-67uy6bann2jjr3vdrmymnq.streamlit.app/",
    },
    {
        "title": "Nivel de crecimiento",
        "image": "data_analisis.png",
        "description": "Análisis del crecimiento y evolución de indicadores clave, pensado para visualizar tendencias y evaluar métricas de rendimiento.",
        "url": "https://appnivelcornarepy-29rycltlbdp2dzs5v32xyl.streamlit.app/",
    },
    {
        "title": "Series de tiempo",
        "image": "Chat_pdf.png",
        "description": "Análisis de series temporales para detectar patrones, comportamientos cíclicos y tendencias que permiten pronosticar eventos futuros.",
        "url": "https://seriesdetiempo-djycav8uu5mi4tjqtceege.streamlit.app/",
    },
    {
        "title": "Suelos",
        "image": "OIG5.jpg",
        "description": "Aplicación orientada al análisis de datos de suelos y variables del terreno, con enfoque en la exploración y evaluación técnica.",
        "url": "https://suelos-lezugsqibpnrcablgafbbr.streamlit.app/",
    },
    {
        "title": "Tasa de aprendizaje",
        "image": "OIG8.jpg",
        "description": "Proyecto dedicado a evaluar la influencia de la tasa de aprendizaje en el entrenamiento de modelos y su impacto en la convergencia.",
        "url": "https://pmendoza1990-tasa-de-aprendizaje-app-gradient-otra-ob8021.streamlit.app/",
    },
]

cols = st.columns(3)
for index, project in enumerate(projects):
    with cols[index % 3]:
        st.subheader(project["title"])
        image = Image.open(project["image"])
        st.image(image, width=210)
        st.write(project["description"])
        st.markdown(f"[Abrir aplicación]({project['url']})")
        st.markdown("---")

st.markdown("---")
st.caption("Portfolio de soluciones basadas en IA, analítica avanzada y aprendizaje automático.")
