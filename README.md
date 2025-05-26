🏁 iRacing Career Stats Viewer
---
A simple and interactive Streamlit web application to visualize and track iRacing career statistics. 
Whether you're monitoring iRating trends, license progress, or race performance over time, this app provides a streamlined way to view your motorsport journey.

🛠️ Tech Stack
---
Frontend/UI: Streamlit

Backend/Data Handling: Python (Pandas, Numpy, Matplotlib/Plotly)

Data Source: Exported data from [Garage61](https://garage61.net/app)

How to see your own stats:
1) Clone this repository.
   git clone https://github.com/BigZeek/iRaceTooMuch.git
   cd iRaceTooMuch
3) Create and activate a virtual environment (optional)
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
4) Install dependencies with "pip install -r requirements.txt"
5) Download your data from Garage61 and add the path to your Excel spreadsheet in the line "racing_data = pd.ExcelFile("your-data-file.xlsx")"
6) Run the application with "streamlit run iRaceApp.py"
