import streamlit as st
from PIL import Image

st.set_page_config(page_title="NeoChat AI", page_icon=":brain:")
st.title("NeoChat AI")
st.subheader("Discutez. Connectez. Réfléchissez.")

logo = Image.open("logo_neochat.png")
st.image(logo, use_column_width=True)

user_input = st.text_input("Posez une question à NeoChat AI :")
if user_input:
    st.success(f"Réponse simulée : '{user_input[::-1]}'")
