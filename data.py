import streamlit as st
import pandas as pd
df=pd.read_csv("Automobile.csv")
st.dataframe(df)
st.bar_chart(df,x="mileage",y="length")
st.scatter_chart(df,x="mileage",y="length")
