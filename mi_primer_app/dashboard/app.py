import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard deportivo", layout="centered")

st.title("Panel de rendimiento: Equipo datos santoto")
st.write("Estadisticas clave de los jugadores del semestre actual")

datos = {
    "Jugador": ["sebastian", "manuel", "crsitian", "gabriela"],
    "Goles": [18, 14, 20, 1],
    "Asistencias": [5, 7, 3, 2],

}
df = pd.DataFrame(datos)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Goles", df["Goles"].sum())
col2.metric("Asistencias", df["Asistencias"].sum())
col3.metric("Goleador del semestre", df.loc[df["Goles"].idxmax(), "Jugador"])
col4.metric("Posicion de liga del equipo", "3°")

st.subheader("Estadisticas al detalle")
st.dataframe(df)

st.subheader("Comparativa de rendiemiento")
st.bar_chart(df.set_index("Jugador"))