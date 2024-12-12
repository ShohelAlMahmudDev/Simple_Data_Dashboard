import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
st.title("Sample Data Dashboard")
uploaded_file=st.file_uploader("Choose a data file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column=st.selectbox("Select column to filter by.",columns)
    unique_values = df[selected_column].unique()
    selected_value=st.selectbox("Select value",unique_values)

    filtered_df=df[df[selected_column]== selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column=st.selectbox("Select x-axis column",columns)
    y_column = st.selectbox("Select y-axis column",columns)

    #Generate Dummy Data for map
    df_map = pd.DataFrame(
        {
            "col1": np.random.randn(1000) / 50 + 37.76,
            "col2": np.random.randn(1000) / 50 + -122.4,
            "col3": np.random.randn(1000) * 100,
            "col4": np.random.rand(1000, 4).tolist(),
        }
        )
    if st.button("Generate Plot"):
        st.subheader("Line Chart")
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        st.subheader("Bar Chart") 
        st.bar_chart(filtered_df.set_index(x_column)[y_column])
        #Generate Map from Dummy Data.
        st.subheader("Map")
        st.map(df_map, latitude="col1", longitude="col2", size="col3", color="col4")
    else:
        st.write("Waiting on file upload...")    