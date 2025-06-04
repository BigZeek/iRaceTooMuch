🏁 iRacing Career Stats Viewer
---
A simple and interactive Streamlit web application to visualize and track iRacing career statistics. 
Whether you're monitoring iRating trends, license progress, or race performance over time, this app provides a streamlined way to view your motorsport journey.

🛠️ Tech Stack
---
Frontend/UI: Streamlit

Backend/Data Handling: Python (Pandas, Plotly)

Data Source: Exported data from [Garage61](https://garage61.net/app)

How to see your own stats:
1) Clone this repository.
   git clone https://github.com/BigZeek/iRaceTooMuch.git
   cd iRaceTooMuch
3) Create and activate a virtual environment (optional)
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
4) Install dependencies with "pip install -r requirements.txt"
5) Download your data from Garage61 and add your data. 
    -**Your page names will be different, and will have to be changed in addition to the initial Excel file read.**
6) Run the application with "streamlit run iRaceApp.py"
**Note: Not all track locations are available on the map. If a track isn't shown it likely needs to be added to the track_locations.csv file.**
**Similarly, not all vehicle images are available to display, and an image may need to be added to the assets folder.**