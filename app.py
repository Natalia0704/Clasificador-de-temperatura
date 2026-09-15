import streamlit as st

st.title("Clasificador de temperatura")

temperatura = st.number_input(
    "Introduce la temperatura en °C:",
    value=20)
if temperatura>=20:
    print("hace calor") 
elif temperatura<=20:
    print("hace frio") 
else:
    print("agradable")
