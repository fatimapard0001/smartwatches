# Smartwatch Health ETL & Dashboard

 This project extracts, cleans, and analyzes smartwatch health data using Python and loads it into a SQLite database.  
An interactive dashboard is built with Streamlit to visualize insights like activity levels, heart rate, and sleep patterns.

# Features
- ETL pipeline (Extract → Transform → Load) in Python
- Data stored in SQLite for analysis
- Interactive dashboard built with Streamlit
- Visualizations: user activity, stress vs. sleep, top users, etc.

# Tech Stack
- Python (pandas, SQLAlchemy, Streamlit)
- SQLite (for data storage)
- VS Code (development environment)

# How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/smartwatches.git

2. Change the 

3. Install dependencies

    pip install -r requirements.txt

4. Make sure that in line 7 to change 'username' to your computer's username or
   change alltogether the relative path of the csv file.
   
5.  Run the ETL pipeline: `index.py` and this will generate 'health_data.db'

6. Running the dashboard
   streamlit run dashboard.py 
   
