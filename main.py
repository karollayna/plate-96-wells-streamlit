# python -m streamlit run .\main.py --server.port 8888

import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title = "Photodynamic treatment", page_icon = ":male-doctor:")

st.title(" :male-doctor: Analysis data from photodynamic therapy")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    data = pd.read_excel(uploaded_file, sheet_name = "Plate_1_Cycle1", header = None)
    data = data.iloc[6:14, 1:13]

    st.write("filename:", uploaded_file.name)

    cell_line = st.text_input("Enter name of cell line for each column separated by space")
    cell_list = cell_line.split()
    cell_lines_df = pd.DataFrame({"cell_lines": cell_list})

    drug_concentration = st.text_input("Enter concentration of drug for each column separated by space")
    concentration_list = drug_concentration.split()
    concentration_list = [float(num) for num in concentration_list]
    drug_concentration_df = pd.DataFrame({"drug_concentration": concentration_list})

    averages = data.mean()
    std = data.std()
    new_data = pd.concat([cell_lines_df, drug_concentration_df, averages, std], axis = 1)
    new_data.columns = ["cell_line", "drug_concentration", "average", "standard_deviation"]
    st.write(new_data)

    fig = px.line(new_data, x='drug_concentration', y='average', color = "cell_line")
    st.plotly_chart(fig)

# bg dx SKG1 SKG1 SKG1 SKG1 SKG1 SKG2 t SKG2 SKG2 SKG2 SKG2
# 0 0 0 5 10 20 40 0 0 5 10 20 40