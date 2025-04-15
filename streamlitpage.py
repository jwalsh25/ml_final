import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="DS 4420 Final Project Extra Credit")

page = st.sidebar.selectbox("Select a Page", ["Landing Page", "MLP Results Visualization"])

if page == "Landing Page":
    st.title("Welcome!")
    st.markdown("""
    This is the web app for our project, Predicting Powerlifting Totals with MLP and Time Series Modeling.
    
    You can access an interactive visualization of our MLP's predicted results as compared to the ground-truth values via the sidebar to the left.
                
    _Charlie Pepin-Woods and Jordan Walsh_
    """)

elif page == "MLP Results Visualization":
    st.title("MLP Results Visualization")
    st.markdown("""
    Below is a plot comparing the total score predictions from our MLP model to the actual values for each competitor. You can use
    the controls to the left to filter the axes (useful for examining outliers), as well as to change the color and size of
    the points in the plot.
    """)

    df_graph = pd.read_csv("df_graph.csv")

    st.sidebar.header("Filters and controls")

    min_actual, max_actual = 0.0, 1200.0
    min_pred, max_pred = 0.0, 1200.0

    actual_range = st.sidebar.slider("Actual Value Range (X-axis)", min_actual, max_actual, (min_actual, max_actual))
    pred_range = st.sidebar.slider("Predicted Value Range (Y-axis)", min_pred, max_pred, (min_pred, max_pred))

    point_color = st.sidebar.color_picker("Pick a color for points", "#1f77b4")
    point_size = st.sidebar.slider("Point size", 10, 100, 30)

    filtered_df = df_graph[
        (df_graph["actual"] >= actual_range[0]) & (df_graph["actual"] <= actual_range[1]) &
        (df_graph["predicted"] >= pred_range[0]) & (df_graph["predicted"] <= pred_range[1])
    ]

    st.subheader("MLP Predictions Plot")
    fig, ax = plt.subplots()
    ax.scatter(filtered_df["actual"], filtered_df["predicted"], color=point_color, s=point_size, alpha=0.6)

    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Predicted vs. Actual")
    ax.set_xlim(min_actual, max_actual)
    ax.set_ylim(min_pred, max_pred)

    st.pyplot(fig)
