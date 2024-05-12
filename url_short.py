
import streamlit as st

import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url



st.set_page_config(page_title="URL Shortener", page_icon="/", layout="centered")
st.image("C:/Users/Javie/OneDrive/Escritorio/Mis proyectos/Acortador Urls/images/www.png", use_column_width=True)
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button ("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))