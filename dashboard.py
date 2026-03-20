import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Cape Town Air Quality", layout="wide", page_icon="🌍")
st.title("🌍 Live Air Quality Intelligence")
st.markdown("Visualizing real-time atmospheric data in Cape Town.")

conn = sqlite3.connect('health_data.db')
query = "SELECT * FROM cape_town_air_quality" 
df = pd.read_sql_query(query, conn)
conn.close()

st.subheader("Current Averages")
col1, col2, col3 = st.columns(3)

with col1:
    avg_pm25 = round(df['pm2_5'].mean(), 2)
    st.metric(label="Avg PM 2.5", value=f"{avg_pm25} µg/m³")
with col2:
    avg_pm10 = round(df['pm10'].mean(), 2)
    st.metric(label="Avg PM 10", value=f"{avg_pm10} µg/m³")
with col3:
    avg_co = round(df['carbon_monoxide'].mean(), 2)
    st.metric(label="Avg Carbon Monoxide", value=f"{avg_co} µg/m³")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🌫️ Particulate Matter", "🚗 Carbon Monoxide", "🗄️ Raw Data"])

with tab1:
    st.subheader("PM 2.5 and PM 10 Trends")
    fig_pm = px.line(df, x='time', y=['pm2_5', 'pm10'], 
                     title="Particulate Matter Concentration",
                     labels={'value': 'Concentration (µg/m³)', 'variable': 'Pollutant'})
    st.plotly_chart(fig_pm, use_container_width=True)

with tab2:
    st.subheader("Carbon Monoxide Levels")
    fig_co = px.area(df, x='time', y='carbon_monoxide', 
                     title="Carbon Monoxide Accumulation",
                     color_discrete_sequence=['#FF4B4B']) 
    st.plotly_chart(fig_co, use_container_width=True)

with tab3:
    st.subheader("Database Feed")
    st.dataframe(df, use_container_width=True)