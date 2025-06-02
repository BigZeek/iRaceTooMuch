import streamlit as st
import pandas as pd
import plotly.express as px
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

disciplineSheet = st.selectbox("Racing Discipline", ("Sports Car", "Formula Car", "Oval", "Dirt Oval", "Dirt Road"))
match disciplineSheet:
        case "Sports Car": 
                iRatingSheet = "IR (Sports Car - Zachery Groen)"
                safetyRatingSheet = "SR (Sports Car - Zachery Groen)"
        case "Formula Car":
                iRatingSheet = "IR (Formula Car - Zachery Groe)"
                safetyRatingSheet = "SR (Formula Car - Zachery Groe)"
        case "Oval":
                iRatingSheet = "IR (Oval - Zachery Groenewold)"
                safetyRatingSheet= "SR (Oval - Zachery Groenewold)"
        case "Dirt Oval":
                iRatingSheet = "IR (Dirt Oval - Zachery Groene)"
                safetyRatingSheet = "SR (Dirt Oval - Zachery Groene)"
        case "Dirt Road":
                iRatingSheet = "IR (Dirt Road - Zachery Groene)"
                safetyRatingSheet = "SR (Dirt Road - Zachery Groene)"
                

iRating = pd.read_excel(racing_data, iRatingSheet)
startDate = iRating['Date'][1].date()
endDate = iRating['Date'].iloc[-1].date()
st.write("From ", startDate, "to ", endDate)

st.write("Discipline iRating")
iRChart = (alt.Chart(iRating)
           .mark_line()
           .encode(alt.Y('iRating').scale(zero=False), x='Date')
           )

st.altair_chart(iRChart, use_container_width=True)

safetyRating = pd.read_excel(racing_data, safetyRatingSheet)
st.write("Discipline Safety Rating")
SRchart = (alt.Chart(safetyRating)
        .mark_line()
        .encode(alt.Y('Safety Rating (raw)').scale(zero=False), x='Date')
        )

st.altair_chart(SRchart, use_container_width=True)
iRating['Date'] = iRating['Date'].dt.date


car_type = pd.read_excel(racing_data, 'Popular cars')
car_label = car_type['Car']
car_laps = car_type['Laps driven']
fig = px.pie(car_type, names=car_label, values=car_laps)
fig.update_traces(textinfo='value')
st.title("Car Use by Laps Driven")
st.plotly_chart(fig)

#Add dynamic most driven car images
most_driven_car = car_type.loc[car_type["Laps driven"].idxmax(), "Car"]
st.title("Most Driven Car:")

match most_driven_car:
        case "Ferrari 296 GT3":
                car_image_string = "assets\Ferrari296GT3-feature-1-1024x576.jpg"
        case "Mercedes-AMG GT4":
                car_image_string = "assets\Mercedes-AMG-GT4-1024x576.jpg"

st.image(car_image_string, caption=most_driven_car)

driving_data = pd.read_excel(racing_data, 'Raw driving data')
grouped = driving_data.groupby("Track")
total_track_laps = grouped["Laps driven"].sum().sort_values(ascending=False)
st.title("Where I Raced")
st.dataframe(data=total_track_laps, use_container_width=False, width=450)

track_df = pd.read_csv("track_locations.csv", encoding = "cp1252", sep="\t")
st.map(track_df)

session_data = pd.read_excel(racing_data, 'Raw driving data')
grouped = driving_data.groupby("Session type")
total_session_laps = grouped["Laps driven"].sum().sort_values(ascending=False)

session_laps_plot = px.bar(total_session_laps, title="Total Laps by Session Type", color=total_session_laps, color_continuous_scale=["red","blue"])
st.plotly_chart(session_laps_plot)
