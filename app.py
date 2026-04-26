import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Carbon Efficiency Dashboard",
    layout="wide"
)


# Load Dataset
df = pd.read_csv("co2_emissions_cleaned.csv")

st.title("Carbon Efficiency Dashboard (CO2 per GDP)")
st.markdown("Analyze carbon efficiency trends across countries over time.")


if "selected_country" not in st.session_state:
    st.session_state.selected_country = sorted(df['country'].dropna().unique())[0]

if "selected_year" not in st.session_state:
    st.session_state.selected_year = int(df['year'].max())

if "selected_country" not in st.session_state:
    st.session_state.selected_country = []


# SECTION 1: COUNTRY ANALYSIS
st.markdown("---")
st.header("Country Trend Over Time")


countries = sorted(df['country'].dropna().unique())
years = sorted(df['year'].dropna().unique())


# Filters
st.sidebar.header("Filters")

countries = sorted(df['country'].dropna().unique())
years = sorted(df['year'].dropna().unique())

selected_country = st.sidebar.selectbox("Select Country", countries)
selected_year = st.sidebar.slider("Select Year", int(min(years)), int(max(years)), int(max(years)))

# Filtered Data
filtered_country_df = df[
    (df['country'] == selected_country) & 
    (df['year'] <= selected_year)
]


# Line Chart
st.subheader("CO2 per GDP Trend Over Time")
st.line_chart(filtered_country_df.set_index('year')['co2_per_gdp'])


# KPI Metrics
st.subheader("Key Metrics")

country_avg = df.groupby('country')['co2_per_gdp'].mean()

max_country = country_avg.idxmax()
min_country = country_avg.idxmin()

max_value = country_avg.max()
min_value = country_avg.min()

col1, col2 = st.columns(2)

col1, col2 = st.columns(2)

with col1:
    st.metric("Most Carbon Intensive", max_country, f"{max_value:.2f}")

with col2:
    st.metric("Most Carbon Efficient", min_country, f"{min_value:.2f}")


# SECTION 2: GLOBAL INSIGHTS
st.markdown("---")
st.header("Global Insights")

# Global Trend
st.subheader("Global Average CO2 per GDP Trend")
global_trend = df.groupby('year')['co2_per_gdp'].mean()
st.line_chart(global_trend)

# Top 10 Highest
top10 = (
    df.groupby('country')['co2_per_gdp']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Top 10 Lowest
bottom10 = (
    df.groupby('country')['co2_per_gdp']
    .mean()
    .sort_values(ascending=True)
    .head(10)
)


# Display side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Carbon Inefficient Countries")
    st.bar_chart(top10)
with col2:
    st.subheader("Top 10 Carbon Efficient Countries")
    st.bar_chart(bottom10)


# SECTION 3: COMPARISON ANALYSIS
st.markdown("---")
st.header("Cross-Country Trend Comparison")

st.sidebar.subheader("Cross-Country Trend Comparison")

default_countries = ["United States", "India"]

selected_countries = st.sidebar.multiselect(
    "Select up to 5 countries",
    countries,
    default=default_countries,
    max_selections=5
)


if selected_countries:
    comparison_df = df[df['country'].isin(selected_countries)]
    comparison = comparison_df.pivot_table(
        index='year',
        columns='country',
        values='co2_per_gdp',
        aggfunc='mean'
    )
    st.line_chart(comparison)
else:
    st.info("Please select at least one country.")


# SECTION 4: DEVELOPMENT ANALYSIS
st.markdown("---")
st.header("Development Analysis")
developed = [
    "Austria", "Belgium", "Denmark", "Finland", "France", "Germany",
    "Greece", "Iceland", "Ireland", "Italy", "Luxembourg", "Netherlands",
    "Norway", "Portugal", "Spain", "Sweden", "Switzerland", "United Kingdom",
    "Czechia", "Estonia", "Latvia", "Lithuania", "Poland", "Slovakia",
    "Slovenia", "Malta", "Cyprus", "Croatia", "Canada", "United States", 
    "Australia", "New Zealand", "Japan", "South Korea", "Singapore", "Israel",
    "United Arab Emirates", "Saudi Arabia", "Bahrain", "Qatar", "Kuwait"
]
df["development_status"] = df["country"].apply(
    lambda x: "Developed" if x in developed else "Developing"
)
selected_year_dev = st.selectbox("Select Year for Comparison", years)
filtered_dev = df[df["year"] == selected_year_dev]
comparison_dev = filtered_dev.groupby("development_status")["co2_per_gdp"].mean()
st.bar_chart(comparison_dev)


# SECTION 5: ADVANCED INSIGHTS
st.markdown("---")
st.header("Advanced Insights")

# CO2 Efficiency Change Over Time
st.subheader("CO2 Efficiency Change Over Time (%)")
trend = df.groupby(["country", "year"])["co2_per_gdp"].mean().reset_index()
trend["pct_change"] = trend.groupby("country")["co2_per_gdp"].pct_change() * 100
avg_change = trend.groupby("year")["pct_change"].mean()
st.line_chart(avg_change)

# Most Improved Countries
st.subheader("Most Improved Countries (CO2 Efficiency)")
df_sorted = df.sort_values(["country", "year"])
improvement = (
    df_sorted.groupby("country")["co2_per_gdp"].first() -
    df_sorted.groupby("country")["co2_per_gdp"].last()
)
st.bar_chart(improvement.sort_values(ascending=False).head(10))

# Insight Text
st.info("Global trends indicate how carbon efficiency has evolved across countries over time.")