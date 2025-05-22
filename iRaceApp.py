import streamlit as st
import numpy as np
import pandas as pd

racing_data = pd.ExcelFile("Garage 61 - Zak Groenewold - Statistics - 2025-05-22-16-01-35.xlsx") #Read entire file in

racing_data.dropna(inplace=True)

#Create dataframes from desired pages
activity_by_day = pd.read_excel(racing_data, 'Activity')

st.title('iRaceTooMuch')
st.write(activity_by_day)