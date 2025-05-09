# src/app.py
import streamlit as st

def add_numbers(a, b):
    return a + b

def multiplication_numbers(a, b):
    return a * b

def soustraction_numbers(a, b):
    return a - b

def division_numbers(a, b):
    return a/b


def main():
    st.title("Bonjour Mme Alessia BRAHITI, j'ai créé une Calculatrice pour toi")
    x = st.number_input("Entrez un nombre", key="x")
    y = st.number_input("Entrez un deuxième nombre", key="y")
    operation=st.selectbox("Choisissez une opération arithmétique : ",["Addition","Soustraction","Multiplication","Division"])
    
    if st.button("Calculer"):
        if operation=="Addition":
            st.write("Résultat:", add_numbers(x, y))
        elif operation=="Soustraction":
            st.write("Résultat:", soustraction_numbers(x, y))  
        elif operation=="Multiplication":
            st.write("Résultat:", multiplication_numbers(x, y))
        elif operation=="Division":
            if y==0:
                st.write("Division par 0 n'est pas possible ! ")
            else:
                st.write("Résultat:", division_numbers(x, y))
        else: 
            st.write("Merci de choisir une opération")




    # 🔁 Point d'entrée local ou via streamlit_app.py
if __name__ == "__main__":
    main()
