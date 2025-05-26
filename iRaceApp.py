import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

racing_data = pd.ExcelFile("Garage 61 - Zak Groenewold - Statistics - 2025-05-22-16-01-35.xlsx") #Read entire file

#Create dataframes from desired pages
activity_by_day = pd.read_excel(racing_data, 'Activity', parse_dates=['Date'])
activity_by_day['Date'] = activity_by_day['Date'].dt.date
activity_by_day['Hours on track'] = activity_by_day['Hours on track'].round(2)
activity_by_day['Clean laps %'] = activity_by_day['Clean laps %'].map("{:.2%}".format)

st.title('iRaceTooMuch')

st.write("Activity by Day", activity_by_day)
st.write("Daily Activity 2025 (This Far!)")
st.line_chart(data=activity_by_day, x='Date', y='Hours on track')

st.selectbox("Racing Discipline", ("Sports Car", "Formula Car"))

sportsCariRating = pd.read_excel(racing_data, 'IR (Sports Car - Zachery Groen)')
st.write("Sports Car iRating All Time")
iRChart = (alt.Chart(sportsCariRating)
           .mark_line()
           .encode(alt.Y('iRating').scale(zero=False), x='Date')
           )

st.altair_chart(iRChart, use_container_width=True)

sportsCarSafetyRating = pd.read_excel(racing_data, 'SR (Sports Car - Zachery Groen)')
sportsCarSafetyRatingRecent = sportsCarSafetyRating.iloc[82:]
st.write("Sports Car Safety Rating 2025")
SRchart = (alt.Chart(sportsCarSafetyRatingRecent)
        .mark_line()
        .encode(alt.Y('Safety Rating (raw)').scale(zero=False), x='Date'))

st.altair_chart(SRchart, use_container_width=True)