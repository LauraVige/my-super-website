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

# Import du fichier qui est dans le repo Github
df_wildflix = pd.read_csv("wildflix_project.csv")


st.write(df_wildflix.head())