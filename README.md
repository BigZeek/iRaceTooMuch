[![wakatime](https://wakatime.com/badge/user/af3e8694-2222-4de2-a458-248b84236d83/project/2887c89c-1602-4733-874e-aaf8b3e19471.svg)](https://wakatime.com/badge/user/af3e8694-2222-4de2-a458-248b84236d83/project/2887c89c-1602-4733-874e-aaf8b3e19471)

🏁 iRacing Career Stats Viewer
---
A simple and interactive Streamlit web application to visualize and track iRacing career statistics. 
Whether you're monitoring iRating trends, license progress, or race performance over time, this app provides a streamlined way to view your motorsport journey.

🛠️ Tech Stack
---
Frontend/UI: Streamlit

Backend/Data Handling: Python (Pandas, Plotly), OpenCage Geocoder    
**This app uses the OpenCage API to fill in track coordinates. You will need your own API key for this functionality.** 

Data Source: Exported data from [Garage61](https://garage61.net/app)

How to see your own stats:
1) Clone this repository.  
   git clone https://github.com/BigZeek/iRaceTooMuch  
   cd iRaceTooMuch
3) Create and activate a virtual environment (optional)  
  python -m venv venv  
  source venv/bin/activate  # On Windows use: venv\Scripts\activate  
4) Install dependencies with "pip install -r requirements.txt"  
5) Download your data from Garage61 and add your data. 
  **Your page names will be different, and will have to be changed in addition to the initial Excel file read.**  
6) Run the application with "streamlit run app.py"  
**The application should add in any missing track locations automatically. If a track is not shown, double check the track_locations.csv file**
**Similarly, not all vehicle images are available to display, and an image may need to be added to the assets folder.**   