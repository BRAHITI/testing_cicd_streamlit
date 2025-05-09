# src/app.py
import streamlit as st

def add_numbers(a, b):
    return a + b

st.title("Addition App")
x = st.number_input("Entrez un nombre", key="x")
y = st.number_input("Entrez un deuxième nombre", key="y")
if st.button("Additionner"):
    st.write("Résultat:", add_numbers(x, y))
