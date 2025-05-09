# src/app.py
import streamlit as st

def add_numbers(a, b):
    return a + b

def multiplication_numbers(a, b):
    return a * b

def soustraction_numbers(a, b):
    return a - b
"""
def div_numbers(a, b):
    try :
        c=a/b
        return c
    except :
        print("Veuillez mettre les bons nombres !")

"""

def main():
    st.title("Calculatrice App")
    x = st.number_input("Entrez un nombre", key="x")
    y = st.number_input("Entrez un deuxième nombre", key="y")
    operation=st.selectbox("Choisissez une opérations arithmétique : ",["Addition","Soustraction","Multiplication","Division"])
    
    if st.button("Calculer"):
        if operation=="Addition":
            st.write("Résultat:", add_numbers(x, y))
        elif operation=="Soustraction":
            st.write("Résultat:", soustraction_numbers(x, y))  
        elif operation=="Multiplication":
            st.write("Résultat:", multiplication_numbers(x, y))
        else: 
            print('Je ne sais pas faire ce calcul ! ')




    # 🔁 Point d'entrée local ou via streamlit_app.py
if __name__ == "__main__":
    main()
