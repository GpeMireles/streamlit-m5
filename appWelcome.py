import streamlit as st

def bienvenida(nombre):
    myMessage = "Bienvenido "+nombre
    return myMessage

myName = st.text_input("Nombre: ")

if (myName):
    
    mensaje = bienvenida(myName)
    st.write(f"Resultado: {mensaje}")