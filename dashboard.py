import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from queries import top_users, sleep_by_stress, steps_by_activity  # <-- import queries

st.title("Smartwatch Health Data Dashboard")

# 1. Top 5 Most Active Users
st.subheader("Top 5 Most Active Users")
st.bar_chart(top_users.set_index("User_ID")["avg_steps"])

# 2. Average Sleep by Stress Level
st.subheader("Average Sleep by Stress Level")
st.line_chart(sleep_by_stress.set_index("Stress_Level")["avg_sleep"])

# 3. Steps by Activity Level
st.subheader("Steps by Activity Level")
st.bar_chart(steps_by_activity.set_index("Activity_Level")["avg_steps"])
