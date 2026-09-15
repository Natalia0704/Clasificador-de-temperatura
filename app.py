import streamlit as st

st.title("Clasificador de temperatura")

temperatura = st.number_input(
    "Introduce la temperatura en °C:",
    value=20)
if temperatura>20:
    st.write("hace calor") 
elif temperatura<20:
    st.write("hace frio") 
else:
    st.write("agradable")
