import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Budget Dashboard")

df = pd.read_excel("budget.xlsx")

total_budget = df["Budget"].sum()
total_realisasi = df["Realisasi"].sum()
sisa = total_budget - total_realisasi

st.title("💰 Budget Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Budget",
    f"Rp {total_budget:,.0f}"
)

col2.metric(
    "Realisasi",
    f"Rp {total_realisasi:,.0f}"
)

col3.metric(
    "Sisa",
    f"Rp {sisa:,.0f}"
)

st.subheader("Penggunaan Budget")

persen = total_realisasi / total_budget

st.progress(float(persen))
st.write(f"{persen:.1%} digunakan")

fig = px.bar(
    df,
    x="Kategori",
    y=["Budget", "Realisasi"],
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Data Detail")
st.dataframe(df)
