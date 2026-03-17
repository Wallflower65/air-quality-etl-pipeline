# 🌬️ Public Health Data Automation: Air Quality ETL Pipeline

## 📌 Project Overview
Environmental factors like particulate matter (PM2.5, PM10) and Carbon Monoxide directly impact respiratory health, driving spikes in clinic admissions for conditions like asthma and COPD. 

This project is a fully automated Data Engineering (ETL) pipeline designed to proactively monitor these triggers. It automatically extracts daily, location-specific air quality data for Cape Town, transforms it into a machine-readable format, and securely loads it into a structured SQL database for health data analysts to query.

## 🧰 Tech Stack
* **Language:** Python
* **Data Extraction:** `requests` (REST API integration)
* **Data Transformation:** `pandas`
* **Database Management:** `sqlite3`
* **Task Automation:** `schedule`

## ⚙️ Pipeline Architecture
1. **Extract:** Connects to the Open-Meteo Air Quality API to pull live, hourly pollutant data (PM10, PM2.5, Carbon Monoxide).
2. **Transform:** Parses the raw JSON payload, standardizes the datetime formats, and structures the unstructured data into a clean Pandas DataFrame.
3. **Load:** Establishes a connection to a local SQLite database (`health_data.db`) and dynamically appends the new daily records to the `cape_town_air_quality` table without duplicating historical data.
4. **Automate:** Utilises a CRON-style background scheduler to execute the entire extraction and loading process autonomously every morning at 06:00 AM.

## 🚀 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required Python dependencies: 
   ```bash
   pip install pandas requests schedule
