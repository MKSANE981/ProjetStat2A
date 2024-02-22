import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image
from st_pages import Page, show_pages, add_page_title

logo = Image.open('Ensai-logo.png')
st.set_page_config(page_title="Scoring credit", page_icon=logo, layout="wide")
add_page_title("Scoring Credit")


st.markdown("""<style>.big-font {font-size: 24px; text-align:justify;} .huge {font-size: 40px;font-weight: bold;} .color{color:green;font-size: 30px;} </style>
        """, unsafe_allow_html=True)