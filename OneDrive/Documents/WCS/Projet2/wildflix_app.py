### Script streamlit pour l'application du projet 2 

# Import des librairies 
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from IPython.display import display, HTML
import streamlit as st

# Ajout titre
st.title('Wildflix project !')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df_mod_daw = pd.read_csv(uploaded_file)

uploaded_file2 = st.file_uploader("Choose a file2")
if uploaded_file2 is not None:
  df = pd.read_csv(uploaded_file2)

# Variables numeriques a prendre en compte 
X = df_mod_daw.select_dtypes('number')