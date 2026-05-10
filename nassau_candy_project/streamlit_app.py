import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from src.data_cleaning import load_data
from src.metrics import calculate_metrics
from src.analysis import top_products
from src.analysis import division_analysis
from src.visualization import profit_chart
from src.visualization import division_chart

st.set_page_config(
    page_title="Nassau Candy Dashboard",
    layout="wide"
)

st.title("Nassau Candy Profitability Dashboard")

# Load data
df = load_data()

# Calculate metrics
df = calculate_metrics(df)

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Gross Profit'].sum()
avg_margin = df['Gross Margin %'].mean()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Average Margin %",
    f"{avg_margin:.2f}%"
)

# Charts
st.header("Top Product Profitability")

top_df = top_products(df)

fig1 = profit_chart(top_df)

st.plotly_chart(fig1)

st.header("Division Performance")

division_df = division_analysis(df)

fig2 = division_chart(division_df)

st.plotly_chart(fig2)

# Dataset
st.header("Dataset Preview")

st.dataframe(df.head(20))