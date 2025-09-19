import pandas as pd
from sqlalchemy import create_engine

# ----------------
# Extract
# ----------------
df = pd.read_csv("/Users/fatimapardesi/Desktop/ETL/venv/unclean_smartwatch_health_data.csv")

# ----------------
# Transform (cleaning)
# ----------------

# Standardize column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Convert numeric columns safely
numeric_cols = ["Heart_Rate_(BPM)", "Blood_Oxygen_Level_(%)", "Step_Count", "Sleep_Duration_(hours)", "Stress_Level"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")  # turns 'ERROR' into NaN

# Fix Activity Level typos
df["Activity_Level"] = df["Activity_Level"].str.strip().str.replace("_", " ")
df["Activity_Level"] = df["Activity_Level"].replace({
    "Actve": "Active",
    "Seddentary": "Sedentary",
    "Highly Active": "Highly Active"
})

# Drop rows with missing User ID
df = df.dropna(subset=["User_ID"])

# Handle Stress Level (mixed text/numeric) – map text to numbers
stress_map = {
    "Very High": 10
}
df["Stress_Level"] = df["Stress_Level"].replace(stress_map)

# ----------------
# Create aggregates (summary data)
# ----------------

# Average stats per user
user_summary = df.groupby("User_ID").agg({
    "Heart_Rate_(BPM)": "mean",
    "Step_Count": "mean",
    "Sleep_Duration_(hours)": "mean",
    "Stress_Level": "mean"
}).reset_index()

# Average by activity level
activity_summary = df.groupby("Activity_Level").agg({
    "Step_Count": "mean",
    "Sleep_Duration_(hours)": "mean",
    "Stress_Level": "mean"
}).reset_index()

# ----------------
# Load into SQLite
# ----------------
engine = create_engine("sqlite:///health_data.db", echo=True)

df.to_sql("raw_health_data", con=engine, if_exists="replace", index=False)
user_summary.to_sql("user_summary", con=engine, if_exists="replace", index=False)
activity_summary.to_sql("activity_summary", con=engine, if_exists="replace", index=False)

print("ETL pipeline completed ")

