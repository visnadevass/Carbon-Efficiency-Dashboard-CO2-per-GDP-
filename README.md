# 🌍 Carbon Efficiency Dashboard (CO₂ per GDP)

## 📊 Project Overview
This project is an interactive data dashboard built using **Streamlit** to analyse global carbon efficiency measured by CO₂ emissions per unit of GDP. It enables users to explore sustainability trends across countries and over time.

The dashboard supports decision-makers, policymakers, and analysts by providing clear visual insights into environmental performance.

---

## 📁 Dataset
- **Name:** CO₂ Emissions per GDP (including land-use change)
- **Source:** World Bank Data (Data360 Platform)
- **Type:** Time-series environmental dataset
- **Scope:** Multiple countries over multiple years

---

## 🎯 Key Features
- Country-wise CO₂ efficiency trend analysis
- Year-based filtering using interactive slider
- Multi-country comparison (up to 5 countries)
- Developed vs Developing country comparison
- Global CO₂ efficiency trend analysis
- Top 10 and Bottom 10 country rankings
- Percentage change analysis over time

---

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- GitHub (Version Control)
- Streamlit Community Cloud (Deployment)

---

## 📊 Dashboard Visualisations
The dashboard includes:
- Time-series line charts
- Comparative bar charts
- Ranking visualisations
- Interactive filters (country & year selection)

---

## 🧪 Testing Summary
The system was tested using structured test cases covering:
- Country filtering functionality
- Year-based filtering
- Multi-country comparison
- Development status classification
- Global trend and ranking validation

All test cases passed successfully.

---

## 🚀 Deployment
The dashboard is deployed using Streamlit Cloud and connected to this GitHub repository.

👉 Live App: https://algp8i4xfiert2qfycrbrc.streamlit.app/

---

## 👨‍💻 Author
Visna Senadi De Vass
Student Project – Data Science Project Lifecycle Coursework

---

## 📸 Dashboard Preview

<img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/48c592e4-20b8-404c-adee-c72b842de8d7" />


<img width="940" height="237" alt="image" src="https://github.com/user-attachments/assets/b20c7535-04fc-4775-baf4-946ec09a5d9c" />


<img width="940" height="397" alt="image" src="https://github.com/user-attachments/assets/75787e67-56ee-4c81-af4c-de4a72d7593a" />


<img width="940" height="412" alt="image" src="https://github.com/user-attachments/assets/5cd4c267-aaf6-4963-a867-922f905adc00" />


<img width="940" height="451" alt="image" src="https://github.com/user-attachments/assets/edfba792-76ab-438e-b378-e68a83097d29" />


<img width="940" height="495" alt="image" src="https://github.com/user-attachments/assets/679fce49-afd5-4ef3-aaf6-f929de60961f" />


<img width="940" height="442" alt="image" src="https://github.com/user-attachments/assets/e7d097e3-60e3-472c-b741-ad63734dcf52" />


<img width="940" height="507" alt="image" src="https://github.com/user-attachments/assets/d59a7b00-059f-4eb7-9b50-bef0434490d3" />


## 📂 Project Structure
- app.py → Main Streamlit application
- co2_emissions_cleaned.csv → Dataset
- requirements.txt → Dependencies

---

## ▶️ Run Locally

1. Clone the repository
```bash
git clone https://github.com/visnadevass/Carbon-Efficiency-Dashboard-CO2-per-GDP-.git
```

2. Navigate to the project folder
```bash
cd Carbon-Efficiency-Dashboard-CO2-per-GDP-
```

3. Install required libraries
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app
```bash
streamlit run app.py
```
