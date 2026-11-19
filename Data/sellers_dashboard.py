import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.title("Sellers Data Dashboard")

# Load sellers Excel file from the same folder as this script
current_folder = Path(__file__).resolve().parent
file_path = current_folder / "sellers.xlsx"
df = pd.read_excel(file_path)

# ---------------------------------
# 1. Data Preview
# ---------------------------------

st.subheader("Data Preview")

st.write(df.head())

# ---------------------------------
# 2. Data Summary
# ---------------------------------

st.subheader("Data Summary")

st.write(df.describe())

# ---------------------------------
# 3. Filter Data by Region
# ---------------------------------

st.subheader("Filter Data by Region")

regions = ["All Regions"] + sorted(
    df["REGION"].dropna().unique().tolist()
)

selected_region = st.selectbox(
    "Select Region",
    regions
)

if selected_region == "All Regions":
    filtered_df = df.copy()
else:
    filtered_df = df[df["REGION"] == selected_region]

st.write(filtered_df)

# ---------------------------------
# 4. Display Graphs
# ---------------------------------

st.subheader("Sales Graphs")

st.write("Units Sold by Vendor")
st.bar_chart(
    filtered_df.set_index("NAME")["SOLD UNITS"]
)

st.write("Total Sales by Vendor")
st.bar_chart(
    filtered_df.set_index("NAME")["TOTAL SALES"]
)

st.write("Average Sales by Vendor")
st.bar_chart(
    filtered_df.set_index("NAME")["SALES AVERAGE"]
)

# ---------------------------------
# 5. Specific Vendor Information
# ---------------------------------

st.subheader("Specific Vendor Information")

vendors = (
    filtered_df["NAME"].astype(str)
    + " "
    + filtered_df["LASTNAME"].astype(str)
).unique().tolist()

if vendors:

    selected_vendor = st.selectbox(
        "Select a Vendor",
        sorted(vendors)
    )

    vendor_names = (
        df["NAME"].astype(str)
        + " "
        + df["LASTNAME"].astype(str)
    )

    vendor_data = df[vendor_names == selected_vendor]

    st.write("Vendor Details")
    st.dataframe(vendor_data)

else:
    st.warning("No vendors available for this region.")

