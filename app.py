import streamlit as st
import numpy as np
import pandas as pd
st.title('Pandamic Covid-19 Death Data Analysis in US')
dataset=pd.read_csv('clean_dataset.csv',usecols=['Lat', 'Long'])
dataset.rename(columns = {'Lat':'LAT'}, inplace = True)
dataset.rename(columns = {'Long':'LON'}, inplace = True)
#st.write(dataset.head())
st.map(dataset)