import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import requests

### Functions ###
def display_individual_discipline():
        iRating = pd.read_excel(racing_data, iRatingData)
        startDate = iRating['Date'][1].date()
        endDate = iRating['Date'].iloc[-1].date()
        st.write("From ", startDate, "to ", endDate)

        current_iRating = iRating['iRating'].iloc[-1]

        st.title("iRating")
        st.metric("Current iRating:", current_iRating)
        iRChart = (alt.Chart(iRating)
                .mark_line()
                .encode(alt.Y('iRating').scale(zero=False), x='Date')
                )

        st.altair_chart(iRChart, use_container_width=True)

        safetyRating = pd.read_excel(racing_data, safetyRatingData)
        st.title("Safety Rating")
        current_safety_rating = safetyRating['Safety Rating'].iloc[-1]
        st.metric("Current Safety Rating:", current_safety_rating)
        SRchart = (alt.Chart(safetyRating)
                .mark_line()
                .encode(alt.Y('Safety Rating (raw)').scale(zero=False), x='Date')
                )

        st.altair_chart(SRchart, use_container_width=True)
        iRating['Date'] = iRating['Date'].dt.date
        
def display_combined_discipline_data():
        ir_sheets = [s for s in racing_data.sheet_names if s.startswith("IR (")]
        sr_sheets = [s for s in racing_data.sheet_names if s.startswith("SR (")]
        
        all_ir_data = []
        for sheet in ir_sheets:
            discipline = sheet.split("(")[1].split(" -")[0]
            df = pd.read_excel(racing_data, sheet_name=sheet)
            df.columns = df.columns.str.strip()
            df = df[["Date", "iRating"]]  
            df["Discipline"] = discipline
            all_ir_data.append(df)

        combined_ir_df = pd.concat(all_ir_data)
        disciplines = combined_ir_df["Discipline"].unique()
        
        selected_disciplines = st.multiselect(
                "Select disciplines to display:",
                options=sorted(disciplines),
                default=sorted(disciplines)
        )
        
        filtered_ir_df = combined_ir_df[combined_ir_df["Discipline"].isin(selected_disciplines)]
        
        fig = px.line(
            filtered_ir_df,
            x="Date",
            y="iRating",
            color="Discipline",
            title="iRating All Disciplines"
        )

        st.plotly_chart(fig, use_container_width=True)
        
        all_sr_data = []
        for sheet in sr_sheets:
            discipline = sheet.split("(")[1].split(" -")[0]
            df = pd.read_excel(racing_data, sheet_name=sheet)
            df.columns = df.columns.str.strip()
            df = df[["Date", "Safety Rating (raw)"]]  
            df["Discipline"] = discipline
            all_sr_data.append(df)
        
        combined_sr_df = pd.concat(all_sr_data)
        disciplines = combined_sr_df["Discipline"].unique()
        
        filtered_sr_df = combined_sr_df[combined_sr_df["Discipline"].isin(selected_disciplines)]
        
        fig = px.line(
            filtered_sr_df,
            x="Date",
            y="Safety Rating (raw)",
            color="Discipline",
            title="Safety Rating All Disciplines"
        )
        
        st.plotly_chart(fig, use_container_width=True)

racing_data = pd.ExcelFile("Garage 61 - Zak Groenewold - Statistics - 2025-06-15-17-20-02.xlsx") #Read entire file

#Create dataframes from desired pages
activity_by_day = pd.read_excel(racing_data, 'Activity', parse_dates=['Date'])
activity_by_day['Date'] = activity_by_day['Date'].dt.date
activity_by_day['Hours on track'] = activity_by_day['Hours on track'].round(2)
activity_by_day['Clean laps %'] = activity_by_day['Clean laps %'].map("{:.2%}".format)

#Get metric data
total_laps = activity_by_day['Laps driven'].sum()
total_clean_laps = activity_by_day['Clean laps'].sum()
tracks_driven = pd.read_excel(racing_data, 'Popular tracks')
most_driven_track = tracks_driven.loc[tracks_driven["Laps driven"].idxmax(), "Track"]
hours_on_track = activity_by_day['Hours on track'].sum().round(2)
clean_lap_value = total_clean_laps/total_laps
clean_lap_percentage = f"{clean_lap_value:.0%}"

st.title('iRaceTooMuch')
col1, col2 = st.columns(2)
with col1: 
        st.metric("Total Laps:",total_laps)
        st.metric("Hours on Track:", hours_on_track)
with col2: 
        st.metric("Clean Laps:", total_clean_laps)
        st.metric("Clean Lap %: ", clean_lap_percentage)
        
st.metric("Most Driven Track:", most_driven_track)


st.write("Activity by Day", activity_by_day)
st.write("Daily Hours on Track")
st.line_chart(data=activity_by_day, x='Date', y='Hours on track')

#iRating and Safety rating visualizations
disciplineSheet = st.selectbox("Racing Discipline", ("Sports Car", "Formula Car", "Oval", "Dirt Oval", "Dirt Road", "All Disciplines"))
match disciplineSheet:
        case "Sports Car": 
                iRatingData = "IR (Sports Car - Zachery Groen)"
                safetyRatingData = "SR (Sports Car - Zachery Groen)"
                display_individual_discipline()
        case "Formula Car":
                iRatingData = "IR (Formula Car - Zachery Groe)"
                safetyRatingData = "SR (Formula Car - Zachery Groe)"
                display_individual_discipline()
        case "Oval":
                iRatingData = "IR (Oval - Zachery Groenewold)"
                safetyRatingData= "SR (Oval - Zachery Groenewold)"
                display_individual_discipline()
        case "Dirt Oval":
                iRatingData = "IR (Dirt Oval - Zachery Groene)"
                safetyRatingData = "SR (Dirt Oval - Zachery Groene)"
                display_individual_discipline()
        case "Dirt Road":
                iRatingData = "IR (Dirt Road - Zachery Groene)"
                safetyRatingData = "SR (Dirt Road - Zachery Groene)"
                display_individual_discipline()
        case "All Disciplines":
                st.write("Note: Road license has been retired as of 2024.")
                display_combined_discipline_data()
        

#Car use visualizations
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
                car_image_string = "assets/Ferrari296GT3-feature-1-1024x576.jpg"
        case "Mercedes-AMG GT4":
                car_image_string = "assets/Mercedes-AMG-GT4-1024x576.jpg"
        case "Chevrolet Corvette Z06 GT3.R":
                car_image_string = "assets\chevrolet-corvette-z06-gt3r-feature-1024x576.jpg"
        case "_":
                st.write("No Available Image")

st.image(car_image_string, caption=most_driven_car)

driving_data = pd.read_excel(racing_data, 'Raw driving data')
grouped = driving_data.groupby("Track")
total_track_laps = grouped["Laps driven"].sum().sort_values(ascending=False)
st.title("Tracks Raced")
st.dataframe(data=total_track_laps, use_container_width=False, width=450)

track_df = pd.read_csv("track_locations.csv", encoding = "cp1252", sep=",")
st.map(track_df)

session_data = pd.read_excel(racing_data, 'Raw driving data')
grouped = driving_data.groupby("Session type")
total_session_laps = grouped["Laps driven"].sum().sort_values(ascending=False)
st.dataframe(total_session_laps)

st.bar_chart(total_session_laps)

st.markdown("---")

st.header("FAQ")

with st.expander("What data is this app using?"):
    st.write("The app uses stats exported from [Garage61](https://garage61.net/app)")

with st.expander("Why is Safety Rating displayed that way?"):
    st.write("Safety Rating has a raw score, but is more commonly read in licenses of A, B, C, D, and R (Rookie). \n More information can be found here: [Safety Rating Explained](https://support.iracing.com/support/solutions/articles/31000156960-iracing-how-to-safety-rating)")

with st.expander("What is iRating?"):
    st.write("A driver skill score based on an ELO type system developed by iRacing. Read about how it works here: [iRating Explained](https://support.iracing.com/support/solutions/articles/31000133523-what-is-irating)")


#Footer for GitHub repo and Latest Commit
st.markdown("---")
st.markdown("🔗 View this project on GitHub")

st.markdown(
    "[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/BigZeek/iRaceTooMuch)"
)

owner = "BigZeek"
repo = "iRaceTooMuch"

url = f"https://api.github.com/repos/{owner}/{repo}/commits"

response = requests.get(url)

if response.status_code == 200:
    latest_commit = response.json()[0]
    message = latest_commit["commit"]["message"]
    date = latest_commit["commit"]["committer"]["date"]
    sha = latest_commit["sha"][:7]
    link = latest_commit["html_url"]

    #st.markdown("---")
    st.markdown(f"🕒 Latest commit: [{sha}]({link}) — _{message}_ 🗓️ {date}")
else:
    st.warning("Could not fetch latest commit info.")
    
    #https://members-ng.iracing.com/web/racing/profile?cust_id=1001966&tab=licenses