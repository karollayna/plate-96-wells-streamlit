import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Photodynamic treatment", page_icon = ":male-doctor:")

st.title(" :male-doctor: Analysis data from photodynamic therapy")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    data = pd.read_excel(uploaded_file, sheet_name = "Plate_1_Cycle1", header = None)
    data = data.iloc[6:14, 1:13]

    st.write("filename:", uploaded_file.name)
    st.write(data)

    averages = data.mean()
    std = data.std()
    new_data = pd.concat([averages, std], axis = 1)
    new_data.columns = ["average", "standard_deviation"]

    cell_line = st.text_input("Enter name of cell line for each column separated by space")
    cell_list = cell_line.split()
    new_data["cell_line"] = cell_list

    drug_concentration = st.text_input("Enter concentration of drug for each column separated by space")
    concentration_list = drug_concentration.split()
    new_data["drug_concentration"] = concentration_list

    st.write(new_data)

    fig = px.line(new_data, x='drug_concentration', y='average', color = "cell_line")
    st.plotly_chart(fig)

