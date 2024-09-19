import streamlit as st 
import numpy as np
import pandas as pd
import time
import plotly.express as px 

info = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title = "Data Science Dashboard",
    page_icon = "☔️",
    layout = "wide"
)

st.title("Real Time-Data science Dashboard")

jobfilter = st.selectbox("select the job",pd.unique(info["job"]))

placeholder = st.empty()

info = info[info["job"] == jobfilter]

for seconds in range(200):
    info["age_new"] = info ["age"] * np.random.choice(range(1,5))
    info["balance_new"] = info ["balance"] * np.random.choice(range(1,5))

    avg_age = np.mean(info["age_new"])
    married_count = int(info[info["marital"] =="married"]["marital"].count() + np.random.choice(range(1,30)))
    avg_balance = np.mean(info["balance_new"])

    with placeholder.container():
        kap1,kap2,kap3 = st.columns(3)

        kap1.metric(label="Age ⏳", value=round(avg_age), delta=round(avg_age) - 10)
        kap2.metric(label="Married Count 💍", value=int(married_count), delta=-10 + married_count)
        kap3.metric(label="A/C Balance ₹", value=f"₹ {round(avg_balance, 2)}", delta=-round(avg_balance / married_count) * 100)

        col1,col2 = st.columns(2)

        with col1:
            st.markdown("Firt Chart(Heatmap)")
            fig1 = px.density_heatmap(
                data_frame=info,
                y = "age_new",
                x = "marital",
                color_continuous_scale="Viridis"
            )
            st.write(fig1)

        with col2:
            st.markdown("Second Chart(Histogram)")
            fig2 = px.histogram(
                data_frame = info,
                x = "age_new",
                color_discrete_sequence=["#F39C12"]
            )
            st.write(fig2)

        st.markdown("Detail Data View")
        st.dataframe(info)
    time.sleep(1)