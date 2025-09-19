import pandas as pd
from sqlalchemy import create_engine

# Connect to the same SQLite database
engine = create_engine("sqlite:///health_data.db")

# 1. Top 5 most active users (by average step count)
query1 = """
SELECT User_ID, AVG(Step_Count) AS avg_steps
FROM raw_health_data
GROUP BY User_ID
ORDER BY avg_steps DESC
LIMIT 5;
"""
top_users = pd.read_sql(query1, engine)
print("\nTop 5 Most Active Users:")
print(top_users)

# 2. Average sleep hours grouped by stress level
query2 = query2 = """
SELECT Stress_Level, AVG("Sleep_Duration_(hours)") AS avg_sleep
FROM raw_health_data
GROUP BY Stress_Level
ORDER BY Stress_Level;
"""

sleep_by_stress = pd.read_sql(query2, engine)
print("\nAverage Sleep by Stress Level:")
print(sleep_by_stress)

# 3. Which activity level burns the most calories (step count as proxy)
query3 = """
SELECT Activity_Level, AVG(Step_Count) AS avg_steps
FROM raw_health_data
GROUP BY Activity_Level
ORDER BY avg_steps DESC;
"""
steps_by_activity = pd.read_sql(query3, engine)
print("\nSteps by Activity Level:")
print(steps_by_activity)


