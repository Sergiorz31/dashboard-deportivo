import streamlit as st
import pandas as pd
st.title("Mi primera aplicación ")
st.write("Bienvenido a mi primera aplicación con python")
st.markdown("Aprendiendo streamlit en visual")
st.write("Esta app muestra informacion de una pagina web")

promedio = 4.2
st.write("El promedio de la pagina es: ", promedio)

datos = pd.DataFrame({
    "Estudiantes": ["Luis", "Maria"],
    "Notas": [4.6, 2.1]

})

st.dataframe(datos)

st.table(datos)

notas = st.slider("Selecciona un rango de notas",
                  min_value=0.0, 
                  max_value=5.0, 
                  value=3.0,
                  step=0.1)
st.write("El rango de notas seleccionado es: ", notas)

carrera = st.selectbox("Seleccione una sola carrera",\
                       ["Ciencias de datos",
                        "Sistemas",
                        "Civil"])
st.write("La carrera seleccionada es: ", carrera)
                